#!/usr/bin/env python3
"""One-shot content refresh for zdzheng.xyz, then commit and push.

Manual workflow (both orders work):
    cd markdown_generator && python3 pubsFromBib.py && cd ..   # rebuild publications
    python3 update_leaderboard.py                              # everything else

or simply:

    python3 update_leaderboard.py     # runs pubsFromBib.py for you

Steps: git pull -> (pubsFromBib.py) -> pull every submodule -> build_blog.py ->
regenerate the four README-based pages -> git add / commit / push.

Flags:
    --skip-pubs        do not run pubsFromBib.py (already ran it yourself)
    --skip-submodules  leave submodules untouched
    --no-push          stop before `git push`

Notes / history:
    * The submodule list is now read from .gitmodules. The hard-coded list this
      script used to carry had drifted: it pulled 8 of the 12 submodules and
      never touched Pytorch-ReID, poster_page, DG-Net or ICME2022SS.
    * Submodules are updated with `fetch` + `merge --ff-only` so a detached HEAD
      still works and a merge commit is never created by accident. Submodules
      with local modifications are skipped rather than clobbered (Pytorch-ReID
      always has one: this script writes its README.md there).
    * Each generated page is fetched *before* anything is written, so a network
      failure leaves the previous page in place instead of deploying a page that
      contains nothing but Jekyll front matter.
    * Python is invoked as sys.executable, i.e. whatever interpreter you started
      this with - pubsFromBib.py needs pybtex/keybert/torch and `python` does not
      always exist on macOS.
"""

import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
SKIP_PUBS = '--skip-pubs' in sys.argv
SKIP_SUBMODULES = '--skip-submodules' in sys.argv
NO_PUSH = '--no-push' in sys.argv

failures = []


def run(cmd, cwd=ROOT, check=True, quiet=False):
    """Run a shell command in an explicit directory. Returns (rc, output)."""
    if not quiet:
        rel = os.path.relpath(cwd, ROOT)
        print(f'\n$ {cmd}' + (f'   [{rel}]' if rel != '.' else ''), flush=True)
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=quiet, text=True)
    if check and r.returncode != 0:
        sys.exit(f'\n!! 命令失败（退出码 {r.returncode}）: {cmd}\n'
                 f'   目录: {cwd}\n   已中止，未提交任何改动。')
    return r.returncode, (r.stdout or '')


def warn(msg):
    failures.append(msg)
    print(f'   !! {msg}', flush=True)


def front_matter(*pairs, closing_blank=True):
    """Build a Jekyll front matter block. pairs is (key, raw_value) and the raw
    value is written verbatim (quotes included)."""
    head = ['---'] + [f'{k}: {v}' for k, v in pairs] + ['---']
    return '\n'.join(head) + ('\n\n' if closing_blank else '\n')


def download(url, min_bytes=500):
    """curl -fsSL to a temp file. Returns the path, or None (and warns) on failure."""
    fd, tmp = tempfile.mkstemp(prefix='ul_')
    os.close(fd)
    rc, _ = run(f'curl -fsSL {url} -o {tmp}', quiet=True)
    if rc != 0:
        warn(f'下载失败，保持原文件不动: {url}')
        os.unlink(tmp)
        return None
    size = os.path.getsize(tmp)
    if size < min_bytes:
        warn(f'下载内容异常（{size} 字节），保持原文件不动: {url}')
        os.unlink(tmp)
        return None
    return tmp


def rebuild_page(dest, head, url):
    """head = front matter text; body is fetched from url. Fetch first, write second."""
    tmp = download(url)
    if tmp is None:
        return
    os.makedirs(os.path.dirname(os.path.join(ROOT, dest)), exist_ok=True)
    with open(tmp, 'r', encoding='utf-8', errors='replace') as f:
        body = f.read()
    os.unlink(tmp)
    with open(os.path.join(ROOT, dest), 'w', encoding='utf-8') as f:
        f.write(head + body)
    print(f'   ok  {dest}  ({len(head) + len(body)} 字节)', flush=True)


def submodule_paths():
    """.gitmodules -> [path]; keeps this script and the submodule list from drifting."""
    out = []
    gm = os.path.join(ROOT, '.gitmodules')
    if not os.path.isfile(gm):
        return out
    with open(gm, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('path'):
                out.append(line.split('=', 1)[1].strip())
    return out


# ---------------------------------------------------------------- 1. 拉取本站
run('git pull --rebase --autostash')

# --------------------------------------------------- 2. 由 .bib 重建 publications
if SKIP_PUBS:
    print('\n-- skip-pubs: 跳过 pubsFromBib.py')
else:
    run(f'"{PY}" pubsFromBib.py', cwd=os.path.join(ROOT, 'markdown_generator'))

# ------------------------------------------------------------ 3. 更新各子模块
if SKIP_SUBMODULES:
    print('\n-- skip-submodules: 跳过子模块')
else:
    print('\n=== 子模块（列表来自 .gitmodules） ===')
    for path in submodule_paths():
        d = os.path.join(ROOT, path)
        if not os.path.isdir(os.path.join(d, '.git')) and not os.path.isfile(os.path.join(d, '.git')):
            warn(f'{path}: 未初始化，跳过（需要时手动 git submodule update --init {path}）')
            continue
        rc, status = run('git status --porcelain', cwd=d, check=False, quiet=True)
        if status.strip():
            warn(f'{path}: 有本地改动，跳过以免覆盖')
            continue
        rc, _ = run('git fetch --quiet origin && git merge --ff-only FETCH_HEAD',
                    cwd=d, check=False, quiet=True)
        if rc == 0:
            print(f'   ok  {path}', flush=True)
        else:
            warn(f'{path}: 更新失败（已跳过，请手动检查）')

# ------------------------------------------------------------------ 4. 重建博客
run(f'"{PY}" build_blog.py', cwd=os.path.join(ROOT, 'scripts'))

# --------------------------------- 5. 四个由「front matter + 上游 README」拼成的页面
print('\n=== 重建 README 页面 ===')

metadataREID = front_matter(
    ('title', '"Pytorch ReID"'),
    ('seo_title', '"Pytorch ReID | Easy to Use"'),
    ('collection', 'pages'),
    ('permalink', '/Pytorch-ReID'),
    ('author_profile', 'false'),
    ('classes', 'wide'),
)
rebuild_page('Pytorch-ReID/README.md', metadataREID,
             'https://raw.githubusercontent.com/layumi/Person_reID_baseline_pytorch/master/README.md')

metadataDA = front_matter(
    ('title', '"Awesome Segmentation Domain Adaptation"'),
    ('seo_title', '"Awesome Segmentation Domain Adaptation | GTA5 -> Cityscapes"'),
    ('collection', 'pages'),
    ('permalink', '/Awesome-SegDA'),
    ('author_profile', 'false'),
    ('classes', 'wide'),
)
rebuild_page('_pages/Awesome-Segmentation-Domain-Adaptation.md', metadataDA,
             'https://raw.githubusercontent.com/layumi/Seg-Uncertainty/master/awesome-SegDA/README.md')

metadataGEO = front_matter(
    ('title', '"Awesome Geo-localization"'),
    ('seo_title', '"Awesome Geo-localization | University1652 CVUSA CVACT Benchmark & SOTA List"'),
    ('description', '"Curated drone and satellite geo-localization resources by Zhedong Zheng '
                    '\u2014 University-1652, CVUSA and CVACT datasets, papers, code and leaderboards."'),
    ('collection', 'pages'),
    ('permalink', '/Awesome-Geo-localization'),
    ('author_profile', 'false'),
    ('classes', 'wide'),
    closing_blank=False,
)
rebuild_page('Awesome-Geolocalization/README.md', metadataGEO,
             'https://raw.githubusercontent.com/layumi/University1652-Baseline/refs/heads/master/State-of-the-art/README.md')

metadataAR = front_matter(
    ('title', '"Awesome reID"'),
    ('seo_title', '"Awesome reID | Benchmark & SOTA List"'),
    ('description', '"Person re-identification benchmark and SOTA leaderboard by Zhedong Zheng '
                    '\u2014 Market-1501, DukeMTMC-reID and MSMT17, with Rank-1 and mAP results."'),
    ('collection', 'pages'),
    ('permalink', '/Awesome-reID'),
    ('author_profile', 'false'),
    ('classes', 'wide'),
    closing_blank=False,
)
rebuild_page('Awesome-reID/README.md', metadataAR,
             'https://raw.githubusercontent.com/layumi/Person_reID_baseline_pytorch/master/leaderboard/README.md')

# --------------------------------------------------------------- 6. 提交并推送
print('\n=== 提交 ===')
run('git add .')
rc, _ = run('git diff --cached --quiet', check=False, quiet=True)
if rc == 0:
    print('   没有改动，跳过 commit/push。')
else:
    run('git commit -m "auto update"')
    if NO_PUSH:
        print('   --no-push：已提交，未推送。')
    else:
        run('git push')

# ------------------------------------------------------------------- 收尾
if failures:
    print('\n=== 以下步骤未成功（其余已完成）===')
    for m in failures:
        print(f'   - {m}')
    sys.exit(1)
print('\n完成。记得本地 bundle exec jekyll build 验证后再确认线上。')
