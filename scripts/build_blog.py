from pathlib import Path
from datetime import date
import yaml
import re

from keybert import KeyBERT

# ========== model ==========
kw_model = KeyBERT(model='all-MiniLM-L6-v2')


def extract_keywords_bert(text, max_keywords=5):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        top_n=max_keywords,
        diversity=0.5
    )

    result = [kw[0].strip().lower() for kw in keywords]

    # 去重 + 简单清洗
    seen = set()
    cleaned = []
    for r in result:
        r = re.sub(r"\s+", " ", r)
        if r not in seen:
            cleaned.append(r)
            seen.add(r)

    return cleaned


# ========== paths ==========
RAW_DIR = Path('../rawblog')
POST_DIR = Path('../_blogs')
POST_DIR.mkdir(exist_ok=True)


def make_slug(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:80]


for md_file in RAW_DIR.glob("*.md"):

    content = md_file.read_text(encoding="utf-8")

    lines = content.splitlines()

    # ===== title =====
    if lines and lines[0].startswith("#"):
        title = lines[0].replace("#", "").strip()
    else:
        title = md_file.stem

    # ===== tags (KeyBERT from full content + title) =====
    text_for_kw = title + ". " + content
    tags = extract_keywords_bert(text_for_kw, max_keywords=6)

    # fallback
    if len(tags) == 0:
        tags = ["blog"]

    # ===== front matter =====
    front_matter = {
        "title": title,
        "date": str(date.today()),
        "permalink": f"/blogs/{make_slug(title)}",
        "tags": tags
    }

    # ====== remove title in the content ========
    content = "\n".join(lines[1:]).lstrip()

    # ===== output =====
    output = (
        "---\n"
        + yaml.dump(
            front_matter,
            allow_unicode=True,
            sort_keys=False,
        )
        + "---\n\n"
        + content
        + "\n\n---\n"
        + "本文首发于郑哲东个人主页：\n"
        + f"https://www.zdzheng.xyz/blogs/{make_slug(title)}\n"
        + "\n转载请注明出处。\n"
    )

    output_name = f"{date.today()}-{make_slug(title)}.md"

    (POST_DIR / output_name).write_text(
        output,
        encoding="utf-8"
    )

    print("Generated:", output_name, "tags:", tags)
