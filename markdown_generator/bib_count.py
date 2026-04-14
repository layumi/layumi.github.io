import re
import sys

def normalize_name(author_str):
    """标准化作者名字： 'Zheng, Zhedong' -> 'Zhedong Zheng'"""
    author_str = author_str.strip().rstrip(',').strip()
    # 移除可能的 "and others"
    author_str = re.sub(r'\band\s+others\b', '', author_str, flags=re.IGNORECASE).strip()
    if ',' in author_str:
        parts = [p.strip() for p in author_str.split(',', 1)]
        if len(parts) == 2 and parts[1]:
            return f"{parts[1]} {parts[0]}".strip()
    return author_str

# UM staff 和 students（精确匹配标准化后的全名）
UM_STAFF = {"Jingrong Liu", "Shaofei Huang", "Zhedong Zheng"}
UM_STUDENTS = {"Hao Ju", "Jiahao Zhang", "Ruiyang Zhang"}
UM_AFFILIATED = UM_STAFF.union(UM_STUDENTS)

def should_skip_venue(venue):
    """如果 venue 包含 ACL 或 Findings of ACL 就跳过"""
    if not venue:
        return False
    v_lower = venue.lower()
    if 'acl' in v_lower or 'findings of acl' in v_lower:
        return True
    return False

def get_venue(entry):
    """提取 venue，优先 booktitle，其次 journal（支持 @article / @misc / @inproceedings 等）"""
    for field in ['booktitle', 'journal']:
        # 修复：f-string + raw string 中大括号需要双写 {{ 和 }}
        match = re.search(rf'{field}\s*=\s*{{([^}}]+)}}', entry, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    return ""

def process_bibtex(bib_content):
    """
    主函数：解析 BibTeX，自动过滤，只统计包含 Zhedong Zheng 的论文
    返回: (total1, total2, total3, papers_counted)
    """
    # 按每个 @ 开头的 entry 分割
    entries = re.split(r'(?=@\w+{)', bib_content.strip())
    
    total1 = 0.0   # (1) 1 / 总作者数 k
    total2 = 0.0   # (2) 1 / UM staff 作者数 m
    total3 = 0.0   # (3) 1 / UM staff+students 作者数 n
    papers_counted = 0
    
    print("🚀 开始处理 BibTeX 文件...\n")
    
    for entry in entries:
        if not entry.strip() or not entry.startswith('@'):
            continue
        
        # 提取作者
        author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE | re.DOTALL)
        if not author_match:
            continue
        authors_str = author_match.group(1)
        
        # 分割作者（支持 "and" 分隔），并自动过滤 "others"
        raw_authors = [a.strip() for a in re.split(r'\s+and\s+', authors_str)]
        raw_authors = [a for a in raw_authors if a.lower() not in ['others', 'and others', '']]
        
        normalized_authors = [normalize_name(a) for a in raw_authors]
        
        # 只处理包含 Zhedong Zheng 的论文
        if "Zhedong Zheng" not in normalized_authors:
            continue
        
        # 提取 venue（用于跳过 ACL）
        venue = get_venue(entry)
        
        if should_skip_venue(venue):
            print(f"⏭️  跳过 ACL/Findings 论文: {venue[:60]}...")
            continue
        
        # 提取 title（仅用于打印）
        title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "Unknown Title"
        
        # 计算三种 weight
        k = len(normalized_authors)
        weight1 = 1.0 / k
        
        staff_in_paper = [a for a in normalized_authors if a in UM_STAFF]
        m = len(staff_in_paper)
        weight2 = 1.0 / m if m > 0 else 0
        
        affiliated_in_paper = [a for a in normalized_authors if a in UM_AFFILIATED]
        n = len(affiliated_in_paper)
        weight3 = 1.0 / n if n > 0 else 0
        
        # 累加
        total1 += weight1
        total2 += weight2
        total3 += weight3
        papers_counted += 1
        
        # 打印每篇详情
        print(f"✅ 计入论文: {title[:80]}...")
        print(f"   Venue: {venue}")
        print(f"   作者总数 k={k} | UM staff m={m} | UM 内部 n={n}")
        print(f"   本篇分数: 1/k={weight1:.4f} | 1/m={weight2:.4f} | 1/n={weight3:.4f}\n")
    
    return total1, total2, total3, papers_counted


# ====================== 主程序 ======================
if __name__ == "__main__":
    # 输入：bib 文件名（命令行参数）
    if len(sys.argv) < 2:
        print("❌ 使用方法: python bib_count.py your_bib_file.bib")
        print("   示例: python bib_count.py my_papers.bib")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            bib_text = f.read()
        print(f"📂 已读取文件: {filename}\n")
    except FileNotFoundError:
        print(f"❌ 错误：文件 '{filename}' 不存在！")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 读取文件出错: {e}")
        sys.exit(1)
    
    # 处理并得到结果
    total1, total2, total3, papers_counted = process_bibtex(bib_text)
    
    # 最终干净输出（符合你的要求）
    print("=" * 70)
    print("🏆 最终统计结果")
    print(f"✅ 考虑的论文总数（不含跳过的 ACL/Findings）: {papers_counted} 篇")
    print(f"累计分数 (1) 1/总作者数          : {total1:.4f}")
    print(f"累计分数 (2) 1/UM staff作者数     : {total2:.4f}")
    print(f"累计分数 (3) 1/UM staff+students : {total3:.4f}")
    print("=" * 70)
