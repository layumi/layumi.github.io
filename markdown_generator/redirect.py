import re
import os

BIB_FILENAME = "pubs.bib"
OUTPUT_BASE = "../files"

def main():
    if not os.path.exists(BIB_FILENAME):
        print(f"找不到文件: {BIB_FILENAME}")
        print("当前目录:", os.getcwd())
        return

    with open(BIB_FILENAME, "r", encoding="utf-8") as f:
        content = f.read()

    # 宽松 pattern：处理空格、换行、{ 前后空白
    pattern = r'url\s*=\s*\{(https?://zdzheng\.xyz/files/[^}]+\.pdf)\}'

    matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)

    print(f"找到 {len(matches)} 个带年份的 PDF 需要重定向")

    if not matches:
        print("没匹配到。打印所有含 'url' 的行供检查：")
        for line in content.splitlines():
            if 'url' in line.lower():
                print("  " + line.strip())
        return

    created = 0

    for url in matches:
        # 提取旧文件名（去掉 .pdf）
        filename = url.split('/')[-1]
        slug = filename.replace(".pdf", "")

        # 创建文件夹 files/旧名.pdf/
        dir_path = os.path.join(OUTPUT_BASE, f"{slug}.pdf")
        os.makedirs(dir_path, exist_ok=True)

        md_path = os.path.join(dir_path, "index.md")

        content_md = f"""---
redirect_to: "{url}"
sitemap: false
---

此 PDF 已永久迁移至新位置：

[{url}]({url})
"""

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(content_md)

        print(f"已生成: {md_path}")
        created += 1

    print(f"\n全部完成，共生成 {created} 个重定向页面。")
    print("请 git add files/ && git commit -m 'add pdf redirects' && git push")
    print("测试示例： https://zdzheng.xyz/files/TMM_jintao_planning.pdf")


if __name__ == "__main__":
    main()
