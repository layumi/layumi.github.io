import re

# 映射：缩写 → 标准格式
venue_mapping_abbr = {
    "CVPR": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
    "ICCV": "IEEE/CVF International Conference on Computer Vision (ICCV)",
    "ECCV": "European Conference on Computer Vision (ECCV)",
    "ACM MM": "ACM International Conference on Multimedia (ACM MM)",
    "ACM MULTIMEDIA": "ACM International Conference on Multimedia (ACM MM)",
    "ICLR": "International Conference on Learning Representations (ICLR)",
    "ICRA": "IEEE International Conference on Robotics and Automation (ICRA)",
    "TMM": "IEEE Transactions on Multimedia (TMM)",
    "TOMM": "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)",
    "TIP": "IEEE Transactions on Image Processing (TIP)",
    "TIFS": "IEEE Transactions on Information Forensics and Security (TIFS)",
    "IJCV": "International Journal of Computer Vision (IJCV)",
    "IJCAI": "International Joint Conference on Artificial Intelligence (IJCAI)",
    "TCSVT": "IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)",
    "PR": "Pattern Recognition (PR)",
    "PRL": "Pattern Recognition Letters (PRL)",
    "TNNLS": "IEEE Transactions on Neural Networks and Learning Systems (TNNLS)",
    "KBS": "Knowledge-Based Systems (KBS)",
    "AAAI": "AAAI Conference on Artificial Intelligence (AAAI)",
    "SIGIR": "ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)"
}

# 生成：全名 → 标准格式（通过反向查找括号前内容）
venue_mapping_fullname = {}
for abbr, full in venue_mapping_abbr.items():
    match = re.match(r"^(.*)\s+\(" + re.escape(abbr) + r"\)$", full)
    if match:
        fullname = match.group(1).strip().upper()
        venue_mapping_fullname[fullname] = full

# 合并成一个总映射：不论是缩写还是全名都能匹配
full_mapping = {}
for key, value in {**venue_mapping_abbr, **venue_mapping_fullname}.items():
    full_mapping[key.upper()] = value

# 编译 regex
venue_pattern = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in full_mapping.keys()) + r")\b",
    re.IGNORECASE
)

def normalize_venue(text: str) -> str:
    def replace(match):
        raw = match.group(0)
        return full_mapping.get(raw.upper(), raw)
    return venue_pattern.sub(replace, text)
