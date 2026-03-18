import re
import os

def extract_year_and_url(entry):
    year_match = re.search(r'year\s*=\s*\{(\d{4})\}', entry, re.IGNORECASE)
    url_match = re.search(r'url\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
    
    year = year_match.group(1) if year_match else None
    url = url_match.group(1).strip() if url_match else None
    
    return year, url

def modify_url(url, year):
    if not url or not year:
        return url
    if 'zdzheng.xyz/files/' not in url:
        return url
    parts = url.split('/files/')
    if len(parts) < 2:
        return url
    filename_part = parts[1].rstrip('}').strip()
    if not filename_part.endswith('.pdf'):
        return url
    new_url = f"https://zdzheng.xyz/files/{year}/{filename_part}"
    return new_url

def process_bib_file(input_file='proceedings.bib', output_file='proceedings_updated.bib'):
    if not os.path.exists(input_file):
        print(f"错误：{input_file} 不存在！请确认文件路径。")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割成独立条目（支持 @inproceedings / @article 等）
    entries = re.split(r'(?=@[a-z]+\{)', content)
    
    modified_entries = []
    move_commands = []
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        
        year, old_url = extract_year_and_url(entry)
        if not year or not old_url:
            modified_entries.append(entry)
            continue
        
        new_url = modify_url(old_url, year)
        if new_url != old_url:
            def repl(match):
                prefix = match.group(1)
                # old_content = match.group(2)  # 不需要
                suffix = match.group(3)
                return f"{prefix}{new_url}{suffix}"
            
            pattern = r'(url\s*=\s*\{)([^}]*)(}\s*,?)'
            entry = re.sub(pattern, repl, entry, flags=re.IGNORECASE | re.DOTALL)
            # 提取 filename
            filename_match = re.search(r'/files/([^/]+\.pdf)', old_url)
            if filename_match:
                filename = filename_match.group(1)
                old_path = f"../files/{filename}"
                new_dir = f"../files/{year}"
                new_path = f"{new_dir}/{filename}"
                
                # 创建目录
                os.makedirs(new_dir, exist_ok=True)
                
                # 生成并执行 mv
                cmd = f'mv -f "{old_path}" "{new_path}"'  # -f 强制覆盖（如果已存在）
                print(f"执行移动: {cmd}")
                os.system(cmd)  # ★★★ 正式运行时取消注释 ★★★
                # 先模拟：
                # print(f"[模拟] {cmd}")
                
                move_commands.append(cmd)
        
        modified_entries.append(entry)
    
    # 保存修改后的 BibTeX
    updated_content = '\n\n'.join(modified_entries).strip()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"\n处理完成！")
    print(f"- 修改后 BibTeX 已保存到: {output_file}")
    print(f"- 总共找到并处理 {len(move_commands)} 个带 url 的条目")
    if move_commands:
        print("前 5 个移动命令示例（实际已执行或模拟）：")
        for cmd in move_commands[:5]:
            print("  " + cmd)
        print("...")

if __name__ == "__main__":
    process_bib_file()
    print("\n建议：运行前先注释 os.system(cmd) 行测试输出；确认无误后再启用真正移动。")
