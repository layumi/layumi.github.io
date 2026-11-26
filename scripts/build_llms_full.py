#!/usr/bin/env python3
# coding: utf-8
"""从 _publications/*.md 重建 llms-full.txt（LLM 抓取用的完整论文清单）。

为什么要生成而不是手写：
    llms-full.txt 是纯静态文件，2026-09-16 之后就没再动过，新论文（SatFix、
    Weather4Geo 等）全部缺席。LLM 走 llms-full.txt 时看不到这些条目，
    这比单个页面的 meta description 影响更大。

用法：
    python3 scripts/build_llms_full.py            # 写回 llms-full.txt
    python3 scripts/build_llms_full.py --check    # 只比对，不写（退出码 1 表示有差异）

格式与 2026-09-16 那版逐字节对齐：条目形如
    - ["标题"](https://zdzheng.xyz/publication/<permalink>): Authors: A, B; Venue: 'V'[; DOI: X]. Abstract: ...
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "_publications")
OUT = os.path.join(ROOT, "llms-full.txt")
SITE = "https://zdzheng.xyz"

HEADER = """# Zhedong Zheng (郑哲东) — Full Publication List

> llms-full.txt companion to https://zdzheng.xyz/llms.txt. Complete publication list with authors, venues, abstracts, and links. Each entry links to the corresponding page on the academic homepage.

Zhedong Zheng is a Tenure-track Assistant Professor at the University of Macau, hosting the AIGC-DL Lab. He received his Ph.D. from UTS (ReLER Lab) and B.S. from Fudan University (2016), and was a postdoctoral fellow at NUS. Research: AIGC, Spatial Intelligence, Data-centric AI, Object Re-identification, Domain Adaptation, Geo-localization, Uncertainty Estimation. H-index 41, 14k+ citations.
"""


def front(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def _unquote(v):
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('\\"', '"')
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


def load_yaml(block):
    """只解析顶层标量字段。

    不引 PyYAML：这个脚本要能在任何一台只装了 Python 的机器上跑，而 frontmatter
    的形状是固定的（一行一个 key，唯一的续行块是 bib: >）。缩进行一律跳过。
    """
    d = {}
    for ln in block.split("\n"):
        if not ln or ln[0] in " \t":
            continue
        m = re.match(r"^([A-Za-z_]+):(.*)$", ln)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if k == "bib":
            break
        d[k] = _unquote(v)
    return d


def authors_of(fm):
    """优先用 author 的 HTML 串（带 - 的全名，如 Tat-Seng Chua）；
    sqlauthor 是机构库侧的写法（Tat Seng Chua），拼出来与人名页不一致。"""
    html = fm.get("author") or ""
    if html:
        s = re.sub(r"<[^>]+>", " ", html)
        s = s.replace("&quot;", '"').replace("&amp;", "&")
        parts = [p.strip(" .") for p in s.split(",")]
        names = [p for p in parts if p]
        if names:
            return ", ".join(names)
    raw = fm.get("sqlauthor") or ""
    if not raw:
        return ""
    try:
        arr = json.loads("[" + raw.strip().rstrip(",") + "]")
        names = [p.get("name", "").strip() for p in arr if p.get("name")]
        if names:
            return ", ".join(names)
    except Exception:
        pass
    # 兜底：正则挖 name
    return ", ".join(re.findall(r'"name":\s*"([^"]+)"', raw))


def clean(s):
    if not s:
        return ""
    s = str(s)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&quot;", '"').replace("&amp;", "&").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()


def collect():
    items = []
    for md in glob.glob(os.path.join(PUB_DIR, "*.md")):
        text = open(md, encoding="utf-8").read()
        fm = load_yaml(front(text))
        if fm.get("sitemap") is False or fm.get("draft") is True:
            continue
        permalink = (fm.get("permalink") or "").strip().rstrip("/")
        title = clean(fm.get("title"))
        if not permalink or not title:
            continue
        year = str(fm.get("pub_year") or "")
        if not year:
            d = str(fm.get("date") or "")
            year = d[:4]
        item = {
            "slug": permalink.rsplit("/", 1)[-1],
            "url": "%s%s" % (SITE, permalink),
            "title": title,
            "authors": authors_of(fm),
            "venue": clean(fm.get("venue")),
            "track": clean(fm.get("track")),
            "doi": (fm.get("doi") or "").strip(),
            "abs": clean(fm.get("abs") or fm.get("abstract")),
            "year": year,
        }
        items.append(item)
    return items


def line_of(it):
    s = '- ["%s"](%s):' % (it["title"], it["url"])
    s += " Authors: %s;" % it["authors"]
    s += " Venue: '%s'" % ((it["venue"] + " - " + it["track"]) if it.get("track") else it["venue"])
    if it["doi"]:
        s += "; DOI: %s" % it["doi"]
    s += "."
    if it["abs"]:
        s += " Abstract: %s" % it["abs"]
    return s


def render(items):
    by_year = {}
    for it in items:
        by_year.setdefault(it["year"], []).append(it)
    out = [HEADER]
    for year in sorted(by_year, reverse=True):
        out.append("## %s" % year)
        out.append("")
        for it in sorted(by_year[year], key=lambda x: x["title"].lower()):
            out.append(line_of(it))
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    items = collect()
    new = render(items)
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    check = "--check" in sys.argv
    if new == old:
        print("llms-full.txt 已是最新（%d 条）" % len(items))
        return 0
    if check:
        import difflib
        d = list(difflib.unified_diff(old.split("\n"), new.split("\n"),
                                      "llms-full.txt(old)", "llms-full.txt(new)", n=0, lineterm=""))
        print("\n".join(d[:60]))
        print("... 差异行数 %d" % len(d))
        return 1
    open(OUT, "w", encoding="utf-8").write(new)
    print("已重写 llms-full.txt：%d 条（%d 字节）" % (len(items), len(new.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
