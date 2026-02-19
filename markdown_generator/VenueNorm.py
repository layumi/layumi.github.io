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
    "TASLP": "IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP)",
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


ccf_info = {
    # 格式: "全名或缩写": (ccf_a: bool, is_acm_ieee: bool, 备注)
    # 人工智能 / 计算机视觉领域
    "CVPR": (True, False),                     # IEEE/CVF → IEEE
    "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)": (True, False),
    "ICCV": (True, False),                      # IEEE/CVF → IEEE
    "IEEE/CVF International Conference on Computer Vision (ICCV)": (True, False),
    "ECCV": (False, False),                    # CCF-B，非 ACM/IEEE
    "European Conference on Computer Vision (ECCV)": (False, False),
    "IJCV": (True, False),                     # Springer，非 ACM/IEEE
    "International Journal of Computer Vision (IJCV)": (True, False),
    "TPAMI": (True, True),                     # IEEE
    "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)": (True, True),
    "ICLR": (False, False),                    # CCF-B
    "International Conference on Learning Representations (ICLR)": (False, False),
    "AAAI": (True, False),                     # AAAI，非 ACM/IEEE
    "AAAI Conference on Artificial Intelligence (AAAI)": (True, False),
    "IJCAI": (True, False),                    # CCF-A，非 ACM/IEEE
    "International Joint Conference on Artificial Intelligence (IJCAI)": (True, False),
    "NeurIPS": (True, False),
    # 多媒体 / 图形学领域
    "ACM MM": (True, False),                    # ACM
    "ACM International Conference on Multimedia (ACM MM)": (True, False),
    "ACM MULTIMEDIA": (True, False),
    "TMM": (False, True),                      # IEEE, CCF-B
    "IEEE Transactions on Multimedia (TMM)": (False, True),
    "TIP": (True, True),                       # IEEE, CCF-A (图形学与多媒体 A 类)
    "IEEE Transactions on Image Processing (TIP)": (True, True),
    "TCSVT": (False, True),                    # IEEE, CCF-B
    "IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)": (False, True),
    "ACM TOMM": (False, True),                 # ACM, CCF-B
    "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)": (False, True),
    "TOMM": (False, True),
    "EMNLP": (False, False), 
    # 其他常见
    "TIFS": (True, True),                      # IEEE, CCF-A (安全领域)
    "IEEE Transactions on Information Forensics and Security (TIFS)": (True, True),
    "TNNLS": (False, True),                    # IEEE, CCF-B
    "IEEE Transactions on Neural Networks and Learning Systems (TNNLS)": (False, True),
    "TCYB": (False, True),                     # IEEE, CCF-B
    "IEEE Transactions on Cybernetics (TCYB)": (False, True),
    "TGRS": (False, True),                     # IEEE, 非计算机类 A
    "IEEE Transactions on Geoscience and Remote Sensing (TGRS)": (False, True),
    "PR": (False, False),                      # Elsevier, CCF-B
    "Pattern Recognition (PR)": (False, False),
    "PRL": (False, False),                     # Elsevier, CCF-C
    "Pattern Recognition Letters (PRL)": (False, False),
    "KBS": (False, False),                     # Elsevier, CCF-B
    "Knowledge-Based Systems (KBS)": (False, False),
    "SIGIR": (True, False),                     # ACM, CCF-A
    "ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)": (True, False),
    "ACM WWW": (True, False),                   # ACM, CCF-A
    "ACM Web Conference (ACM WWW)": (True, False),
    "WWW": (True, False),
    "TASLP": (False, True),                    # IEEE/ACM, 通常 CCF-B
    "IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP)": (False, True),
    "ICRA": (False, False),                     # IEEE, CCF-B
    "IEEE International Conference on Robotics and Automation (ICRA)": (False, False),
}

def check_venue(venue_name: str):
    venue_name = venue_name.strip()
    key = venue_name.upper() if venue_name.isupper() else venue_name  # 尝试匹配缩写或全名
    if "Workshop" in key or "Workshops" in key:
        return 0,0,0
    # 尝试直接匹配
    if key in ccf_info:
        is_ccf_a, is_acm_ieee = ccf_info[key]
    else:
        # 尝试模糊匹配（简单包含）
        found = False
        for k, v in ccf_info.items():
            if venue_name.lower() in k.lower() or k.lower() in venue_name.lower():
                is_ccf_a, is_acm_ieee = v
                found = True
                break
        if not found:
            print(venue_name+"not defined!")
            return 0,0,0  # 未找到
    return 1, 1 if is_ccf_a else 0, 1 if is_acm_ieee else 0

if __name__ == "__main__":
    print(normalize_venue('International Journal of Computer Vision (IJCV)'))
