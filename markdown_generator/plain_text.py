# -*- coding: utf-8 -*-
"""把 bib 摘要里的 LaTeX 标记转成网页 / LLM 可直接读的纯文本。

**只用于 `abs:` 字段（页面上的可视摘要）。** `bib:` 块必须保留原始 BibTeX ——
那份是给人复制进 .tex 的，LaTeX 标记在那里是正确写法，不能清洗。

为什么是定点替换而不是通用 LaTeX 解析器：本仓库 96 篇摘要实测只有 7 种形态
（\\% ×63、\\& ×3、\\eg ×3、$\\times$ ×3、~ ×3、\\ie ×2、\\\\% ×2），
没有花括号、没有 \\textit 之类。定点表足够，且不会误伤正文。

注意 `~` 故意不处理：三个实例都是「约 11.3%」的意思，不是 LaTeX 不断行空格，
换成普通空格会丢掉"约"的语义。

`\\&gt;` 这种是 HTML 实体混进了 LaTeX（proceedings.bib 里写作
"GTA5 -\\&gt; Cityscapes"），所以实体规则必须排在 `\\&` 规则之前。
"""
import re

_SUBS = [
    # HTML 实体混进 LaTeX —— 必须最先处理，否则 \&gt; 会被下面的 \& 规则吃掉一部分。
    # 注意这里还原的是实体本身（&gt; 就是 ">"），不要自作聪明补成 "->"：
    # 原文是 "GTA5 -\&gt; Cityscapes"，那个 "-" 本来就在，补了会变成 "-->"
    (re.compile(r"\\?&gt;"), ">"),
    (re.compile(r"\\?&lt;"), "<"),
    (re.compile(r"&amp;"), "&"),
    # 转义符号（\\{1,2} 同时覆盖 \% 与 \\%）
    (re.compile(r"\\{1,2}%"), "%"),
    (re.compile(r"\\{1,2}&"), "&"),
    # 行内数学
    (re.compile(r"\$\s*\\times\s*\$"), "×"),
    (re.compile(r"\$([^$]*)\$"), r"\1"),
    (re.compile(r"\\times\b"), "×"),
    # 常见缩写命令
    (re.compile(r"\\eg\b"), "e.g."),
    (re.compile(r"\\ie\b"), "i.e."),
    (re.compile(r"\\etal\b"), "et al."),
    (re.compile(r"\\etc\b"), "etc."),
    (re.compile(r"\\wrt\b"), "w.r.t."),
    (re.compile(r"\\cf\b"), "cf."),
    # 兜底：去掉剩余反斜杠命令的标记，保留词本身
    (re.compile(r"\\([a-zA-Z]+)"), r"\1"),
]


def to_plain_text(s):
    """清洗摘要文本；输入为空时原样返回。"""
    if not s:
        return s
    t = s
    for pat, rep in _SUBS:
        t = pat.sub(rep, t)
    return t
