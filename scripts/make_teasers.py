#!/usr/bin/env python3
# coding: utf-8
"""把每篇论文 PDF 的首页渲成 1200×630 的分享图（og:image），并把路径写进 md 的 frontmatter。

用法（在仓库任意位置都能跑，路径按脚本自身定位）：
    python3 scripts/make_teasers.py            # 只补新的/变过的
    python3 scripts/make_teasers.py --force    # 全部重做
    python3 scripts/make_teasers.py --limit 5  # 只做前 5 篇，调试用

为什么单独一个脚本，而不是塞进 pubsFromBib.py：
  * pubsFromBib.py 的职责是 bib → markdown，纯文本转换，不该依赖 PDF 渲染库；
  * 渲染一张图要几十到几百毫秒，99 篇就是几秒到几十秒，塞进去会让每次重建都变慢；
  * 这是**可增量**的工作（PDF 没变就跳过），和重建整站无关；
  * 渲染失败不该让整站重建失败，分开跑可以各自重试。

依赖：优先 PyMuPDF（`pip install pymupdf`，跨平台）；没有就退回 macOS 的 sips
（质量差一些，整页缩到 630 高再补白边）。两者都没有就跳过、不写 frontmatter。
"""

import os
import re
import subprocess
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "_publications")
OUT_DIR = os.path.join(ROOT, "images", "teaser")
CARD_W, CARD_H = 1200, 630          # og:image 建议尺寸
QUALITY = 82


def read_front(text):
    # 注意：部分 md 的结尾 --- 后面没有换行，所以不能要求 \n---\n
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def field(front, name):
    m = re.search(r"^%s:\s*(.*)$" % name, front, re.M)
    if not m:
        return ""
    return m.group(1).strip().strip("'\"")


def local_pdf(url):
    """把 site 上的 PDF 地址映射回仓库里的文件；外部链接返回 None。"""
    if not url:
        return None
    u = url.strip()
    i = u.find("/files/")
    if i < 0:
        return None
    path = os.path.join(ROOT, u[i + 1:])
    return path if os.path.isfile(path) else None


def _pymupdf():
    """新版包名是 pymupdf，旧版是 fitz；两个都试，避免 FutureWarning。"""
    try:
        import pymupdf
        return pymupdf
    except Exception:
        import fitz
        return fitz


def render_pymupdf(pdf, out):
    fitz = _pymupdf()

    doc = fitz.open(pdf)
    page = doc[0]
    r = page.rect
    # 先找页面最上面一块正文的位置，跳过页眉留白（ACM/IEEE 模板顶部常有一大条空白，
    # 直接按 y0 裁会有一成多的死白）。找不到文本就退回页顶。
    top = r.y0
    try:
        ys = [b[1] for b in page.get_text("blocks") if b[4].strip()]
        if ys:
            top = max(r.y0, min(ys) - 8)
    except Exception:
        pass
    # 取 1200:630 的横条，标题、作者、摘要开头基本都在里面
    strip_h = min(r.y1 - top, r.width / (CARD_W / CARD_H))
    clip = fitz.Rect(r.x0, top, r.x1, top + strip_h)
    zoom = CARD_W / clip.width
    pix = page.get_pixmap(clip=clip, matrix=fitz.Matrix(zoom, zoom), alpha=False)
    # PyMuPDF 把裁剪框换算到设备像素时会按行取整，实测约四成页面出来是 631 行，
    # 与 JSON-LD 里声明的 1200×630 不符。直接按行重采样，砍掉底部多出的那一行。
    if pix.height > CARD_H:
        w, n, stride = pix.width, pix.n, pix.stride
        rows = [pix.samples[y * stride:y * stride + w * n] for y in range(CARD_H)]
        pix = fitz.Pixmap(pix.colorspace, w, CARD_H, b"".join(rows), pix.alpha)
    pix.save(out, jpg_quality=QUALITY)
    doc.close()
    return "pymupdf"


def render_sips(pdf, out):
    """macOS 兜底：整页渲染 → 缩到 630 高 → 补白到 1200×630。"""
    tmp_png = out + ".page.png"
    tmp_fit = out + ".fit.png"
    subprocess.run(["sips", "-s", "format", "png", pdf, "--out", tmp_png],
                   check=True, capture_output=True)
    subprocess.run(["sips", "--resampleHeight", str(CARD_H), tmp_png, "--out", tmp_fit],
                   check=True, capture_output=True)
    subprocess.run(["sips", "--padToHeightWidth", str(CARD_H), str(CARD_W),
                    "--padColor", "FFFFFF", tmp_fit, "--out", tmp_fit],
                   check=True, capture_output=True)
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", str(QUALITY),
                    tmp_fit, "--out", out], check=True, capture_output=True)
    for p in (tmp_png, tmp_fit):
        if os.path.exists(p):
            os.remove(p)
    return "sips"


def pick_renderer():
    try:
        _pymupdf()
        return render_pymupdf
    except Exception:
        pass
    if sys.platform == "darwin":
        return render_sips
    return None


def inject_og_image(md_path, url_path):
    """在 frontmatter 的 permalink 行后写一行 og_image（幂等）。"""
    text = open(md_path, encoding="utf-8").read()
    line = "og_image: '%s'" % url_path
    if re.search(r"^og_image:.*$", text[:2000], re.M):
        new = re.sub(r"^og_image:.*$", line, text, count=1, flags=re.M)
    else:
        new = re.sub(r"^(permalink:.*)$", r"\1\n" + line, text, count=1, flags=re.M)
    if new != text:
        open(md_path, "w", encoding="utf-8").write(new)
        return True
    return False


def main():
    force = "--force" in sys.argv
    limit = None
    for i, a in enumerate(sys.argv):
        if a == "--limit" and i + 1 < len(sys.argv):
            limit = int(sys.argv[i + 1])

    renderer = pick_renderer()
    if renderer is None:
        print("✗ 没有可用的 PDF 渲染器：请 pip install pymupdf（macOS 也可直接用 sips）")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(PUB_DIR, "*.md")))
    if limit:
        files = files[:limit]

    made = skipped = failed = injected = 0
    for md in files:
        text = open(md, encoding="utf-8").read()
        front = read_front(text)
        permalink = field(front, "permalink")
        pdf = local_pdf(field(front, "paperurl"))
        if not permalink or not pdf:
            skipped += 1
            continue
        slug = permalink.rstrip("/").rsplit("/", 1)[-1]
        out = os.path.join(OUT_DIR, slug + ".jpg")
        url_path = "/images/teaser/%s.jpg" % slug

        if (not force and os.path.exists(out)
                and os.path.getmtime(out) >= os.path.getmtime(pdf)):
            pass
        else:
            try:
                renderer(pdf, out)
                made += 1
            except Exception as e:
                print("  ✗ %s: %s" % (slug, str(e)[:120]))
                failed += 1
                continue
        if os.path.exists(out) and inject_og_image(md, url_path):
            injected += 1

    print("分享图：新生成 %d，跳过 %d（无本地 PDF），失败 %d；写入 og_image %d 篇。输出目录 %s"
          % (made, skipped, failed, injected, os.path.relpath(OUT_DIR, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
