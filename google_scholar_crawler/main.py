"""Fetch citation data from Google Scholar for the personal homepage.

Design notes
------------
Google aggressively rate-limits datacenter IPs (GitHub Actions runners live in
Azure ranges that are heavily abused by scrapers).  When Google returns 403,
scholarly's internal retry loop can only rotate the session cookie -- with no
proxy configured it cannot change the exit IP, so after `_max_retries` attempts
it raises MaxTriesExceededException.

Empirically this job succeeded only ~20% of the time over 2026-03..2026-09.
So the strategy here is:

1. Give scholarly a longer, more patient internal retry budget (more attempts,
   longer per-request timeout).
2. Retry the *whole* fetch at this level too, sleeping between rounds, because
   a fresh round builds brand-new sessions with fresh cookies.
3. If every round fails, exit with a distinct status (75) instead of crashing,
   so the workflow can treat "Google said no today" as a soft failure and keep
   the previously published numbers rather than showing an error.
"""

import json
import os
import random
import sys
import time
from datetime import datetime

from scholarly import scholarly

SCHOLAR_ID = 'XT17oUEAAAAJ'

# Whole-run retry budget. Each round internally performs `MAX_INTERNAL_RETRIES`
# attempts, so the total number of HTTP requests is bounded by the product.
MAX_ROUNDS = 4
MAX_INTERNAL_RETRIES = 10
REQUEST_TIMEOUT = 30
BASE_SLEEP = 20          # seconds before round 2, grows linearly
JITTER = 15              # random additional seconds, de-synchronises from cron

EXIT_ANTI_BOT = 75       # distinct code: Google refused, not a code bug


def _configure_scholarly() -> None:
    """Widen scholarly's retry/timeout envelope for flaky datacenter IPs."""
    scholarly.set_retries(MAX_INTERNAL_RETRIES)
    scholarly.set_timeout(REQUEST_TIMEOUT)


def _fetch_author():
    """One fetch round: resolve the author id and fill all sections."""
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

    author = None
    for round_index in range(1, MAX_ROUNDS + 1):
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
            if round_index < MAX_ROUNDS:
                nap = BASE_SLEEP * round_index + random.uniform(0, JITTER)
                print(f'[round {round_index}] sleeping {nap:.1f}s before retry',
                      flush=True)
                time.sleep(nap)

    if author is None:
        print(f'ALL {MAX_ROUNDS} ROUNDS FAILED (anti-bot).', flush=True)
        return EXIT_ANTI_BOT

    _write_results(author)
    return 0


if __name__ == '__main__':
    sys.exit(main())
