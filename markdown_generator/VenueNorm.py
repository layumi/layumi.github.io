import re

# 映射：缩写 → 标准格式
venue_mapping_abbr = {
    "CVPR": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
    "ICCV": "IEEE/CVF International Conference on Computer Vision (ICCV)",
    "ECCV": "European Conference on Computer Vision (ECCV)",
    "ACM MM": "ACM International Conference on Multimedia (ACM MM)",
    "ACM MULTIMEDIA": "ACM International Conference on Multimedia (ACM MM)",
    "ACM TOMM": "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)",
    "ICLR": "International Conference on Learning Representations (ICLR)",
    "ICRA": "IEEE International Conference on Robotics and Automation (ICRA)",
    "TCYB": "IEEE Transactions on Cybernetics (TCYB)",
    "TMM": "IEEE Transactions on Multimedia (TMM)",
    "TOMM": "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)",
    "TIP": "IEEE Transactions on Image Processing (TIP)",
    "TIFS": "IEEE Transactions on Information Forensics and Security (TIFS)",
    "TGRS": "IEEE Transactions on Geoscience and Remote Sensing (TGRS)",
    "IJCV": "International Journal of Computer Vision (IJCV)",
    "IJCAI": "International Joint Conference on Artificial Intelligence (IJCAI)",
    "TCSVT": "IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)",
    "PRL": "Pattern Recognition Letters (PRL)",
    "PR": "Pattern Recognition (PR)",
    "TNNLS": "IEEE Transactions on Neural Networks and Learning Systems (TNNLS)",
    "KBS": "Knowledge-Based Systems (KBS)",
    "AAAI": "AAAI Conference on Artificial Intelligence (AAAI)",
    "TPAMI": "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)",
    "ACM WWW": "ACM Web Conference (ACM WWW)",
    "WWW": "ACM Web Conference (ACM WWW)",
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

# 构建匹配 venue 的 regex（不匹配已带缩写括号的形式）
venue_pattern = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in sorted(full_mapping.keys(), key=lambda x: -len(x))) + r")\b(?!\s*\()", 
    re.IGNORECASE
)
standard_format_regex = re.compile(r"\([A-Z]{2,10}\)")

def normalize_venue(text: str) -> str:
    # 如果整段文本中已经有标准 venue 格式 "(XYZ)"，说明是规范化后的 venue，跳过
    if standard_format_regex.search(text):
        return text
    def replace(match):
        raw = match.group(0)
        raw_upper = raw.upper()
        return full_mapping.get(raw_upper, raw)

    return venue_pattern.sub(replace, text)

if __name__ == "__main__":
    print(normalize_venue('International Journal of Computer Vision (IJCV)'))
