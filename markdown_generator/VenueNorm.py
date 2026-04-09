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
    "TVCG": "IEEE Transactions on Visualization and Computer Graphics",
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
    "npj AI": "npj Artificial Intelligence",
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
    "CVPR": (True, False, True, False),                     # IEEE/CVF → IEEE
    "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)": (True, False, True, False),
    "ICCV": (True, False, True, False),                      # IEEE/CVF → IEEE
    "IEEE/CVF International Conference on Computer Vision (ICCV)": (True, False, True, False),
    "ECCV": (False, False, True, False),                    # CCF-B，非 ACM/IEEE
    "European Conference on Computer Vision (ECCV)": (False, False, True, False),
    "IJCV": (True, False, False, True),                     # Springer，非 ACM/IEEE
    "International Journal of Computer Vision (IJCV)": (True, False, False, True),
    "TPAMI": (True, True, False, True),                     # IEEE
    "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)": (True, True, False, True),
    "ICLR": (False, False, True, False),                    # CCF-B
    "International Conference on Learning Representations (ICLR)": (False, False, True, False),
    "AAAI": (True, False, True, False),                     # AAAI，非 ACM/IEEE
    "AAAI Conference on Artificial Intelligence (AAAI)": (True, False, True, False),
    "IJCAI": (True, False, True, False),                    # CCF-A，非 ACM/IEEE
    "International Joint Conference on Artificial Intelligence (IJCAI)": (True, False, True, False),
    "NeurIPS": (True, False, True, False),
    # 多媒体 / 图形学领域
    "ACM MM": (True, False, True, False),                    # ACM
    "ACM International Conference on Multimedia (ACM MM)": (True, False, True, False),
    "ACM MULTIMEDIA": (True, False, True, False),
    "TMM": (False, True, False, True),                      # IEEE, CCF-B
    "IEEE Transactions on Multimedia (TMM)": (False, True, False, True),
    "TIP": (True, True, False, True),                       # IEEE, CCF-A (图形学与多媒体 A 类)
    "IEEE Transactions on Image Processing (TIP)": (True, True, False, True),
    "TCSVT": (False, True, False, True),                    # IEEE, CCF-B
    "IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)": (False, True, False, True),
    "ACM TOMM": (False, True, False, True),                 # ACM, CCF-B
    "ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)": (False, True, False, True),
    "TOMM": (False, True, False, True),
    "TVCG": (True, True, False, True),
    "IEEE Transactions on Visualization and Computer Graphics": (True, True, False, True),
    "npj Artificial Intelligence": (False, False, False, True),   
    "EMNLP": (False, False, True, False), 
    "Findings of ACL": (False, False, True, False), 
    "ACL": (True, False, True, False), 
    # 其他常见
    "TIFS": (True, True, False, True),                      # IEEE, CCF-A (安全领域)
    "IEEE Transactions on Information Forensics and Security (TIFS)": (True, True, False, True),
    "TNNLS": (False, True, False, True),                    # IEEE, CCF-B
    "IEEE Transactions on Neural Networks and Learning Systems (TNNLS)": (False, True, False, True),
    "TCYB": (False, True, False, True),                     # IEEE, CCF-B
    "IEEE Transactions on Cybernetics (TCYB)": (False, True, False, True),
    "TGRS": (False, True, False, True),                     # IEEE, 非计算机类 A
    "IEEE Transactions on Geoscience and Remote Sensing (TGRS)": (False, True, False, True),
    "PR": (False, False, False, True),                      # Elsevier, CCF-B
    "Pattern Recognition (PR)": (False, False, False, True),
    "PRL": (False, False, False, True),                     # Elsevier, CCF-C
    "Pattern Recognition Letters (PRL)": (False, False, False, True),
    "KBS": (False, False, False, True),                     # Elsevier, CCF-B
    "Knowledge-Based Systems (KBS)": (False, False, False, True),
    "SIGIR": (True, False, True, False),                     # ACM, CCF-A
    "ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)": (True, False, True, False),
    "ACM WWW": (True, False, True, False),                   # ACM, CCF-A
    "ACM Web Conference (ACM WWW)": (True, False, True, False),
    "WWW": (True, False, True, False),
    "TASLP": (False, True, False, True),                    # IEEE/ACM, 通常 CCF-B
    "IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP)": (False, True, False, True),
    "ICRA": (False, False, True, False),                     # IEEE, CCF-B
    "IEEE International Conference on Robotics and Automation (ICRA)": (False, False, True, False),
}

def check_venue(venue_name: str):
    is_ccf_a, is_acm_ieee, is_conf, is_trans = False, False, False, False
    venue_name = venue_name.strip()
    key = venue_name.upper() if venue_name.isupper() else venue_name  # 尝试匹配缩写或全名
    if "Workshop" in key or "Workshops" in key:
        print(venue_name+'is a workshop!')
        return 0,0,0,0,0
    if "arXiv" in key or "arxiv" in key:
        print(venue_name+'is an arXiv!')
        return 0,0,0,0,0
    # 尝试直接匹配
    if key in ccf_info:
        is_ccf_a, is_acm_ieee, is_conf, is_trans = ccf_info[key]
    else:
        # 尝试模糊匹配（简单包含）
        found = False
        for k, v in ccf_info.items():
            if venue_name.lower() in k.lower() or k.lower() in venue_name.lower():
                is_ccf_a, is_acm_ieee, is_conf, is_trans = v
                found = True
                break
        if not found:
            print(venue_name+"not defined!")
            return 0,0,0,0,0  # 未找到
    if is_trans: print("trans:"+venue_name)
    return 1, 1 if is_ccf_a else 0, 1 if is_acm_ieee else 0, 1 if is_conf else 0, 1 if is_trans else 0

if __name__ == "__main__":
    print(normalize_venue('International Journal of Computer Vision (IJCV)'))
