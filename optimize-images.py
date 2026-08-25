#!/usr/bin/env python3
"""
optimize-images.py — zdzheng.xyz 首页图片瘦身脚本
依据 Google PageSpeed 移动端报告（2026-08-25）：
  每张图的下载尺寸远超显示尺寸，resize 到实际显示上限即可清零 "Improve image delivery"。

用法（在站点仓库根目录）：
  python3 optimize-images.py

前置：pip install pillow
说明：自动备份原图到 images-backup-YYYYMMDD/，覆盖同名文件。
      推完 git 后建议在 Cloudflare 后台 purge 一次 images/ 缓存（静态资源 TTL 4h）。
"""
from PIL import Image
import os, shutil, datetime

BACKUP = f"images-backup-{datetime.date.today():%Y%m%d}"
os.makedirs(BACKUP, exist_ok=True)

# (相对路径, 目标宽度px, quality)
# 目标宽度依据：
#   talk 缩略图最大显示 662px（桌面 16:9）→ 700px 留余量
#   profile 头像桌面 sidebar ~200px、移动端 63px → 400px 兼顾 JSON-LD 引用
#   lab-logo 显示 210px → 220px；red/green 显示 88px → 90px
TASKS = [
    ("images/uav.webp",       700, 78),   # 1918x1078 -> 700x393
    ("images/retid.webp",     700, 78),   # 1728x970  -> 700x393
    ("images/asi.webp",       700, 78),   # 2800x1578 -> 700x394 (体积降 ~4x)
    ("images/profile.webp",   400, 80),   # 1024x720  -> 400x281
    ("images/profile2.webp",  400, 80),
    ("images/profile3.webp",  400, 80),
    ("resource-img/lab-logo-trans.webp", 220, 80),  # 702x562 -> 220x176
    ("images/red.webp",        90, 75),   # 243x178  -> 90x66
    ("images/green.webp",      90, 75),   # 118x87   -> 90x66
]

total_before = 0
total_after = 0
for path, width, q in TASKS:
    if not os.path.exists(path):
        print(f"跳过(不存在): {path}")
        continue
    before = os.path.getsize(path)
    total_before += before
    shutil.copy(path, os.path.join(BACKUP, os.path.basename(path)))
    im = Image.open(path).convert("RGB")
    if im.width > width:
        h = round(im.height * width / im.width)
        im = im.resize((width, h), Image.LANCZOS)
    im.save(path, "WEBP", quality=q, method=6)
    after = os.path.getsize(path)
    total_after += after
    print(f"OK {path}: {im.size[0]}x{im.size[1]}  {before//1024}KB -> {after//1024}KB  (省 {max(0,(before-after))//1024}KB)")

print(f"\n合计: {total_before//1024}KB -> {total_after//1024}KB  省 {(total_before-total_after)//1024}KB")
print(f"备份在 {BACKUP}/")
