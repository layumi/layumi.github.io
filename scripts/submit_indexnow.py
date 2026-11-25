#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把站点 URL 推给 IndexNow（Bing / Yandex / Seznam 等共用端点）。

Google 不参与 IndexNow，它只能走 sitemap + Search Console，所以这个脚本只解决
「Bing 侧多久重新抓」的问题。

key 文件必须已经部署在站点根目录、内容与文件名一致，否则端点返回 403。
本仓库的 key 是 dfd88821f5124a23883543e712b1d8ad.txt，改 key 时这两处要一起改。

用法：
    python3 scripts/submit_indexnow.py                 # 推所有 /publication/ 页 + 列表页 + 首页
    python3 scripts/submit_indexnow.py --all           # 推 sitemap 里全部 URL
    python3 scripts/submit_indexnow.py --prefix /authors/
    python3 scripts/submit_indexnow.py --url https://zdzheng.xyz/publication/Progress2026
    python3 scripts/submit_indexnow.py --dry-run       # 只打印，不发请求
"""
import argparse
import json
import re
import sys
import urllib.request

HOST = "zdzheng.xyz"
KEY = "dfd88821f5124a23883543e712b1d8ad"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
SITEMAP = f"https://{HOST}/sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
DEFAULT_PREFIXES = ("/publication/", "/publications/", "/")


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "zdzheng-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "ignore")


def sitemap_urls():
    status, body = fetch(SITEMAP)
    if status != 200:
        sys.exit(f"sitemap 拉取失败：HTTP {status}")
    return re.findall(r"<loc>(.*?)</loc>", body)


def _match(path, p):
    # "/" 只匹配首页本身，不能当通配前缀用，否则前缀表会把全站都吃进来
    if p == "/":
        return path == "/"
    return path == p or (p.endswith("/") and path.startswith(p))


def pick(urls, prefixes):
    out = []
    for u in urls:
        path = u[len(f"https://{HOST}"):] or "/"
        if any(_match(path, p) for p in prefixes):
            out.append(u)
    return sorted(set(out))


def submit(batch_urls, dry=False):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": batch_urls,
    }
    data = json.dumps(payload).encode("utf-8")
    print(f"  POST {ENDPOINT} | {len(batch_urls)} 条 URL | {len(data)} 字节")
    if dry:
        print("  [dry-run] 未发请求")
        return
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "zdzheng-indexnow/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8", "ignore").strip()
            print(f"  HTTP {r.status} {r.reason} {body[:200]}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore").strip()
        # 200/202 = 已接受；403 = key 校验失败；422 = URL 不属于该 host；429 = 频率限制
        sys.exit(f"  HTTP {e.code} {e.reason} {body[:300]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="推 sitemap 全部 URL")
    ap.add_argument("--prefix", action="append", default=[], help="只推指定路径前缀，可重复")
    ap.add_argument("--url", action="append", default=[], help="只推指定 URL，可重复")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.url:
        urls = a.url
    else:
        urls = sitemap_urls()
        prefixes = () if a.all else (a.prefix or list(DEFAULT_PREFIXES))
        urls = pick(urls, prefixes)
        if not urls:
            sys.exit("筛选后没有 URL，检查 --prefix")

    print(f"待推 {len(urls)} 条：{urls[0]} … {urls[-1]}")
    for i in range(0, len(urls), 10000):
        submit(urls[i:i + 10000], dry=a.dry_run)


if __name__ == "__main__":
    main()
