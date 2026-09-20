"""Fetch citation data from Google Scholar for the personal homepage.

Why this file looks the way it does
-----------------------------------
Google rate-limits datacenter IPs hard, and GitHub Actions runners live in
Azure ranges that scrapers have burned.  Two facts drive the whole design:

1. **scholarly's 403 handler is very slow.**  With no proxy configured, every
   attempt after the first sleeps ``random.uniform(60, 120)`` seconds, and then
   ``_get_page`` re-runs the entire loop through its "premium" path, doubling
   the cost.  Measured: ``set_retries(10)`` makes a single blocked fetch take
   ~28 minutes.  An earlier revision combined that with 4 outer rounds and
   burned **116 minutes of runner time and still published nothing.**

   => Therefore this script deliberately keeps scholarly's internal retry
      budget at 1 and does its own retrying.  Retrying is cheap here: the
      expensive part is scholarly's internal backoff, not our loop.

2. **The exit IP is what Google judges, and we cannot change it.**  A fresh
   round does rebuild session + cookies, which is the only lever available
   without a paid proxy.  So resilience comes from *many cheap rounds spaced
   out in time*, not from one long patient attempt.

The outer loop therefore:
  * makes up to ``MAX_ROUNDS`` quick attempts,
  * spaces them with jittered backoff (de-synchronising from the cron schedule),
  * and exits 75 on total failure so the caller can tell "Google refused"
    apart from "the code is broken".
"""

import json
import os
import random
import sys
import time
from datetime import datetime

from scholarly import scholarly

SCHOLAR_ID = 'XT17oUEAAAAJ'

# One attempt is allowed a handful of quick internal retries -- enough to ride
# out a transient blip, few enough that a hard block is detected in seconds
# rather than minutes.  RAISE THIS ONLY IF YOU HAVE VERIFIED THE TIMING:
# each internal retry after the first can cost up to 120s x 2 (secondary +
# premium path), so set_retries(5) already means ~15 min per attempt.
MAX_INTERNAL_RETRIES = 2
REQUEST_TIMEOUT = 20

MAX_ROUNDS = 8           # cheap attempts, spaced out
BASE_SLEEP = 20          # seconds; grows linearly per round
JITTER = 25              # random extra seconds, avoids cron-locked patterns
MAX_TOTAL_SECONDS = 20 * 60   # global wall-clock ceiling, checked between rounds

EXIT_ANTI_BOT = 75       # distinct code: Google refused, not a code bug


def _configure_scholarly() -> None:
    """Keep scholarly's own retry budget minimal; we retry at this level."""
    scholarly.set_retries(MAX_INTERNAL_RETRIES)
    scholarly.set_timeout(REQUEST_TIMEOUT)


def _fetch_author():
    """One attempt: resolve the author id and fill all sections."""
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(
        author,
        sections=['basics', 'indices', 'counts', 'publications'],
    )
    return author


def _is_anti_bot_error(exc: BaseException) -> bool:
    """Distinguish 'Google refused us' from genuine bugs.

    Anything raised out of scholarly's own proxy/navigator layer means the
    request never got a usable answer -- that is the anti-bot path, not a
    programming error.
    """
    name = type(exc).__name__
    if name in ('MaxTriesExceededException', 'DOSException'):
        return True
    module = type(exc).__module__ or ''
    return 'scholarly' in module


def _write_results(author) -> None:
    author['updated'] = str(datetime.now())
    author['publications'] = {
        v['author_pub_id']: v for v in author['publications']
    }
    print(json.dumps(author, indent=2))

    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        'schemaVersion': 1,
        'label': 'citations',
        'message': f"{author['citedby']}",
    }
    with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    print('wrote results/gs_data.json and results/gs_data_shieldsio.json',
          flush=True)


def main() -> int:
    _configure_scholarly()
    started = time.time()

    author = None
    attempts = 0
    for round_index in range(1, MAX_ROUNDS + 1):
        attempts = round_index
        try:
            print(f'[round {round_index}/{MAX_ROUNDS}] fetching {SCHOLAR_ID} ...',
                  flush=True)
            author = _fetch_author()
            print(f'[round {round_index}] ok: {author.get("name")} '
                  f'citedby={author.get("citedby")}', flush=True)
            break
        except Exception as exc:                      # noqa: BLE001
            print(f'[round {round_index}] failed: '
                  f'{type(exc).__name__}: {str(exc)[:200]}', flush=True)
            if not _is_anti_bot_error(exc):
                # A real bug -- fail loudly and immediately, do not mask it.
                raise

        if round_index >= MAX_ROUNDS:
            break
        nap = BASE_SLEEP * round_index + random.uniform(0, JITTER)
        if time.time() - started + nap > MAX_TOTAL_SECONDS:
            print('[budget] wall-clock ceiling reached; stopping retries',
                  flush=True)
            break
        print(f'[round {round_index}] sleeping {nap:.1f}s before retry',
              flush=True)
        time.sleep(nap)

    elapsed = time.time() - started
    if author is None:
        print(f'::error::Google Scholar refused all {attempts} attempt(s) '
              f'after {elapsed / 60:.1f} min. Citation data NOT updated; '
              f'published numbers are unchanged.', flush=True)
        return EXIT_ANTI_BOT

    _write_results(author)
    print(f'success in {elapsed / 60:.1f} min', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
