# zdzheng.xyz — academic homepage of Zhedong Zheng (AIGC-DL Lab, University of Macau)

Source of **https://zdzheng.xyz**. Jekyll site forked (then detached) from
[academicpages](https://github.com/academicpages/academicpages.github.io), itself a fork of
[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/). MIT — see `LICENSE`.

**Read this before editing.** One half of this repo is hand-written, the other half is generated
and *wiped* by a script. The two workflows are described below and they are not interchangeable.

---

## Deploy

Push to `master` → GitHub Pages builds (Jekyll 3.10, ~30 s, ~693 HTML pages) → live in 1–2 min.
`CNAME` pins the domain, Cloudflare sits in front. `vercel.json` also sits in the repo (it defines
redirects such as `/more2024` → `/MORE2024`); the deployment observed from outside is GitHub Pages
+ Cloudflare.

| Response | Cache header | Consequence |
|---|---|---|
| HTML | `max-age=0, must-revalidate` | an edit shows up immediately |
| static assets — `assets/`, `images/`, fonts | `max-age=14400` | **4-hour window where a visitor gets new HTML + old CSS** |

That second row has bitten twice: a newly added control appeared but its stylesheet was missing,
so the button wrapped onto its own line and clicking it did nothing. It is now handled
structurally — `assets/css/main.scss` defines `$ct-asset-version` from `site.time`, and the same
value is appended as `?v=` in **four** places:

1. `main.css` preload **and** stylesheet (`_includes/head.html`)
2. `main.min.js` (`_includes/scripts.html`)
3. `@font-face` URLs in `_sass/vendor/font-awesome/solid.scss` and `brands.scss`

Keep all four identical. (Without the font one, a cached font hides newly added icons.) Anything
else you add under `assets/` should be versioned the same way.

## Where things live

| I want to change… | Edit | Notes |
|---|---|---|
| Homepage body, **News**, hero, stats cards | `_pages/about.md` | hand-maintained; front matter holds `seo_title` / `excerpt` (= title & meta description) |
| Publications, authors, tags, funding | **never** `_publications/`, `_authors/`, `_tag/`, `_funding/` | generated, and wiped on every run of `pubsFromBib.py` |
| The publication data itself | `markdown_generator/proceedings.bib` (conferences), `pubs.bib` (journals) | one BibTeX entry per paper |
| Nav bar | `_data/navigation.yml` | |
| Site title / description / og:image / URL | `_config.yml` | |
| `<head>`, meta, JSON-LD | `_includes/head.html`, `_includes/seo.html` | |
| Sidebar, avatar, social links | `_includes/author-profile.html` | |
| Archive (paper list) cards | `_includes/archive-single.html` | shared by `publications/`, `blogs/`, tags |
| Styling / light-dark theme | `assets/css/main.scss`, `_sass/` | see "Theme" |
| AI-facing summary (GEO) | `llms.txt` (short, curated), `llms-full.txt` (~170 KB) | keep the paper-count wording self-labelled: "80+ published", "90+ incl. preprints" |
| Talks, teaching, portfolio, posts | `_talks/`, `_teaching/`, `_portfolio/`, `_posts/` | |

## Content workflow A — publications (generated)

```bash
cd markdown_generator && python3 pubsFromBib.py && cd ..   # rebuild publications
python3 update_leaderboard.py                              # everything else
```

`update_leaderboard.py` runs `pubsFromBib.py` itself, so you can either do both steps manually or
just run the second one. Flags: `--skip-pubs`, `--skip-submodules`, `--no-push`.

**`pubsFromBib.py`** (needs `pybtex`, `keybert`, `sentence-transformers`, `torch`) empties and
rebuilds the four generated collections from the two `.bib` files — venue normalisation lives in
`markdown_generator/VenueNorm.py`, keywords come from KeyBERT — and then **regex-rewrites the
paper-count sentence inside** `_pages/publications.md`, `_pages/recruitment_en.md` and
`_pages/recruitment.md`.

> ⚠️ **Do not reword those three sentences.** The script replaces a fixed pattern; if the pattern
> stops matching it *inserts a second copy* instead of replacing. If the wording really must
> change, update the patterns at the bottom of `pubsFromBib.py` in the same commit. The English
> pattern also hard-codes “9 are ESI highly cited papers”.

Permalinks are `<first 10 characters of the title><year>`, e.g. the BibTeX key
`zhang2026vsearcher` for *VSearcher: Long-Horizon Multimodal Search Agent…* is published at
`/publication/VSearche2026`. **Copy the `permalink:` out of the generated markdown — never guess
it** when linking from News or the homepage.

**`update_leaderboard.py`** additionally: `git pull --rebase --autostash` → updates every
submodule (list read from `.gitmodules`) → `scripts/build_blog.py` → regenerates four pages by
writing Jekyll front matter and appending the upstream README (`Pytorch-ReID/README.md`,
`_pages/Awesome-Segmentation-Domain-Adaptation.md`, `Awesome-Geolocalization/README.md`,
`Awesome-reID/README.md`) → `git add .`, commit, **push**. It pushes for you. Each remote README is
downloaded *before* anything is written, so a network failure leaves the previous page intact
instead of deploying a page with nothing but front matter.

## Content workflow B — News (hand-written)

`_pages/about.md` has one `<h2 class="mag">…News</h2>` followed by a single `<ul>`; older items
live in a `<details><summary>Past News (2025-2020)</summary>` block. Keep entries in rough
reverse-chronological order, newest first, one `<li>` per item, tab-indented.

```html
<li> <strong>NeurIPS 2026:</strong> <a href="https://zdzheng.xyz/publication/VSearche2026">Multimodal Search Agent</a></li>
```

- `<strong>Venue Year:</strong>` first — use the same separator style as the surrounding lines.
- Anchor text is a **2–4 word label for the work**, not the full title.
- Several papers: `N papers - ` followed by comma-separated links.
- Awards: `<span class="oral-tag">(<i class="fas fa-star"></i>Oral)</span>` — values used so far: `Oral`, `Highlight`.
- Grants: `<li><strong>PI</strong>, FDCT/0209/2025/AMJ, 2026–2029, MOP 1.66M</li>`.
- When the list grows long, move the oldest entries into the `Past News` details block.

## Local build & verify

```bash
bundle exec jekyll build                 # ~28 s, ~693 pages, output in _site/ (git-ignored)
grep -o '<title>[^<]*</title>' _site/index.html
grep -o '<meta name="description" content="[^"]*"' _site/index.html
```

**Always build before pushing** — a Liquid or SCSS error otherwise only shows up after deploy.
Spot-check the paper pages too (`_site/publication/<Permalink>.html`).

## Theme (light / dark)

`_sass/_cosmos-theme.scss` is imported **last** in `assets/css/main.scss`. It only overlays
tokens; the Minimal Mistakes components are untouched, so the light path cannot regress. Full
revert = delete that file + its one `@import`.

- **Modes**: `auto` (default) → dark when the visitor's local clock is in the night window
  (`NIGHT_START` / `NIGHT_END`, currently 19:00–06:59, in `_includes/head.html`) **or** their
  system is dark; plus `light` / `dark`. An explicit choice is stored in `localStorage.theme` and
  always wins. The button cycles auto → light → dark.
- **One source of truth**: the no-flash script in `_includes/head.html`, which runs before the
  stylesheet (no white flash for dark visitors) and exposes `window.__ctTheme`.
  `_includes/scripts.html` only drives the button — do not re-implement the resolution.
- **Tokens** are `--ct-*`; `:root` = light, `html[data-theme="dark"]` = dark, and the two sets
  must stay in sync. `--ct-bg` is the page background (one step below `--ct-surface` in dark).
- Section 3 of the theme file (the ~88 component overrides) is **generated** by
  `theme-rules-gen.py --baseline <a main.css built before the theme layer> --apply`. Regenerate it
  rather than hand-editing. The hand-written `@media (min-width: 57.8125em)` reset immediately
  after it is deliberate and must stay.
- Three inline `<style>` blocks outrank the stylesheet and are tokenised too: `_pages/about.md`,
  `_includes/archive-single.html`, `_includes/head/custom.html` (plus `_pages/resources.md`, which
  uses page-local `--res-*` variables).
- If you ever rebuild `assets/js/main.min.js` (`npm run uglify`), delete the theme handler block in
  `_includes/scripts.html` — that bundle already contains MM's own theme code and clicks would
  double-fire.

## Traps that have actually bitten

- **BSD grep**: macOS `grep` does not support `\|` alternation and **silently returns 0 matches**.
  Always `grep -E 'a|b'`. This once produced a completely wrong “the code was already removed”
  conclusion.
- **`grep -c` counts lines, not matches** — on a minified one-line CSS/JS it is always 1. Use
  `grep -o … | wc -l`.
- **Don't drop the `?v=` from the CSS / JS / font URLs** (see Deploy).
- **Auditing “is this tokenised?”**: overrides are *appended*, so the original literal is still
  present in the built CSS. The real question is whether the same selector + property has a
  `var(--ct-…)` override *later in the file* that resolves — under light tokens — back to the
  original literal.
- **Headless verification**: `chrome-headless-shell` screenshots are racy (retry and keep the
  image with the most distinct colours); `file://` renders but a local HTTP server came out blank;
  `document.styleSheets[…].cssRules` throws on `file://`. Preferred method: inject a script that
  writes `getComputedStyle` values into `document.title` and read it back with `--dump-dom`.
  If the page has `transition: all .2s`, disable transitions first — otherwise you read the
  *pre-transition* colour and misdiagnose. Same family of trap: the auto theme removes a
  hand-injected `data-theme="dark"`; call `window.__ctTheme.apply('dark')` instead.
- **`Pytorch-ReID` is an uninitialised submodule** that `update_leaderboard.py` writes a generated
  `README.md` into; that file is **not tracked by this repo**.

## Scripts

| Script | Purpose |
|---|---|
| `update_leaderboard.py` | refresh submodules + generated pages, commit and push |
| `markdown_generator/pubsFromBib.py` | rebuild the four generated collections from `.bib`; rewrites paper-count sentences |
| `markdown_generator/bib_count.py` | count entries per venue in the `.bib` files |
| `scripts/build_blog.py` | regenerate the blog index |
| `theme-rules-gen.py` | regenerate the theme's token overrides from a pre-theme `main.css` |
| `optimize-images.py` | resize/recompress `images/` + `resource-img/` down to displayed size |
| `talkmap.py` | build the talk cluster map (run from `_talks/`; needs `getorg`/`geopy`) |

## Submodules

`.gitmodules` is the source of truth (12 entries: `poster_page`, `DG-Net`, `ICME2022SS`,
`ACMMM2023Workshop`, `Pytorch-ReID`, `MORE2024`, `ACMMM2024Workshop-UAV`, `MORE2025`,
`ACMMM2025Workshop-UAV`, `synthir26`, `ACMMM2026Workshop-UAV`,
`Awesome-Aerial-Spatial-Intelligence`). `update_leaderboard.py` reads that list, so the two can no
longer drift apart; it skips uninitialised or locally modified submodules and says so rather than
clobbering them.

## Lineage

Forked and detached from
[academicpages](https://github.com/academicpages/academicpages.github.io) (© Stuart Geiger), built
on [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (© Michael Rose),
MIT-licensed. `CHANGELOG.md` is the upstream template's changelog and is no longer maintained here.
