#!/usr/bin/env python3
"""
主题规则生成器 —— 把 Minimal Mistakes 组件里硬编码的浅色值换成 CSS 变量（token），
           使 _sass/_cosmos-theme.scss 的暗色主题能整体翻转。

为什么需要脚本而不是手写：
    组件用的是一组很接近的灰（#494e52 / #7a8288 / #5c6266 / #9ba1a6 / #777a7d /
    #bdc1c4 / #dee0e1 / #f2f3f3 / #fafafa …），同一个值在不同属性上语义不同
    （#fff 既当文字色也当底色，#7a8288 既当文字色也当按钮填充）。手工映射曾经把
    blockquote / .toc / .greedy-nav / .author__urls 的浅色值取错，也会漏掉重复选择器。
    这里改为从「引入主题层之前的构建产物」程序化推导，浅色值 = 原字面值，因此
    浅色渲染在数学上不可能改变。

用法
----
1. 取得基线 CSS（引入主题层之前的产物，仓库里不跟踪 _site，所以要临时构建一次）：

     git stash push _sass/_cosmos-theme.scss assets/css/main.scss
     bundle exec jekyll build && cp _site/assets/css/main.css /tmp/baseline_main.css
     git stash pop

   （或者用任意一次未包含主题层的 CI 产物。）

2. 干跑，看会生成什么、有没有没映射的颜色：

     python3 theme-rules-gen.py --baseline /tmp/baseline_main.css

3. 写回主题文件第 3 节：

     python3 theme-rules-gen.py --baseline /tmp/baseline_main.css --apply

4. 一定会顺带跑的两项校验（本脚本不含，见 README/记忆）：
   - 构建后的 main.css 里，基线每个颜色字面值都应有同名选择器的 token 覆盖，
     且用浅色 token 解析回来的值必须等于原字面值；
   - 全站 HTML 内联样式引用的 --ct-* 必须都在 :root 里有定义。

注意：@media 上下文必须保留。基线里存在「窄屏写样式、宽屏重置为 transparent」这类
     成对规则（如 .author__urls），而重置那一条通常不含颜色字面值、不会被生成，
     所以 _cosmos-theme.scss 第 3 节末尾手写了一段同断点的重置，不能删。
"""
import argparse
import re
import sys
from collections import Counter, defaultdict

# 字面值 -> token。分属性上下文，因为同一个值当"文字色"和当"底色"语义不同。
# 浅色 token 的取值必须等于字面值本身（保证浅色零回归）。
TEXT = {
    '#fff': '--ct-on-accent', '#ffffff': '--ct-on-accent',
    '#494e52': '--ct-text', '#7a8288': '--ct-mid', '#5c6266': '--ct-text-hover-2',
    '#9ba1a6': '--ct-text-mute', '#777a7d': '--ct-text-fig',
    '#bdc1c4': '--ct-border-2', '#dee0e1': '--ct-border-3',
    '#52adc8': '--ct-link', '#3e8296': '--ct-link-hover', '#000': '--ct-strong',
}
FILL = {
    '#fff': '--ct-surface', '#ffffff': '--ct-surface',
    '#7a8288': '--ct-fill', '#f2f3f3': '--ct-border',
    '#fafafa': '--ct-surface-2', '#dee0e1': '--ct-border-3',
    '#bdc1c4': '--ct-border-2', '#000': '--ct-hero-bg', '#52adc8': '--ct-link',
    '#494e52': '--ct-text',
}
BORDER = {
    '#f2f3f3': '--ct-border', '#bdc1c4': '--ct-border-2', '#dee0e1': '--ct-border-3',
    '#7a8288': '--ct-mid', '#494e52': '--ct-text', '#000': '--ct-strong',
    '#fff': '--ct-surface', '#52adc8': '--ct-link',
}
LITERALS = set(TEXT) | set(FILL) | set(BORDER)


def pick(prop, sel, lit):
    """按属性语义挑 token。"""
    if prop.startswith('background'):
        if sel.strip() in ('html', 'body'):
            return '--ct-bg'          # 页面底色，暗色下比 surface 更深
        for m in (FILL, BORDER, TEXT):
            if lit in m:
                return m[lit]
    elif 'color' in prop or prop.endswith('fill') or prop.endswith('stroke'):
        for m in (TEXT, BORDER, FILL):
            if lit in m:
                return m[lit]
    else:
        for m in (BORDER, FILL, TEXT):
            if lit in m:
                return m[lit]
    return None


def split_decls(body):
    """按 ; 切声明，但尊重引号与括号（data URI 里可能含分号）。"""
    out, buf, depth, q = [], '', 0, None
    for ch in body:
        if q:
            if ch == q:
                q = None
            buf += ch
        elif ch in '"\'':
            q = ch
            buf += ch
        elif ch == '(':
            depth += 1
            buf += ch
        elif ch == ')':
            depth -= 1
            buf += ch
        elif ch == ';' and depth == 0:
            out.append(buf)
            buf = ''
        else:
            buf += ch
    if buf.strip():
        out.append(buf)
    return [d.strip() for d in out if d.strip()]


def parse(css):
    """返回 [(ctx_list, selector, body)]，ctx_list 为该规则的 @media/@supports 祖先链。"""
    out, ctx, buf = [], [], ''
    i, n = 0, len(css)
    while i < n:
        c = css[i]
        if c == ';' and not ctx:          # 顶层 @charset/@import 语句
            buf = ''
            i += 1
            continue
        if c == '{':
            head = buf.strip()
            buf = ''
            if head.startswith('@media') or head.startswith('@supports'):
                ctx.append(head)
                i += 1
                continue
            if head.startswith('@'):      # @font-face / @keyframes：整块跳过
                depth, j = 1, i + 1
                while j < n and depth > 0:
                    if css[j] == '{':
                        depth += 1
                    elif css[j] == '}':
                        depth -= 1
                    j += 1
                i = j
                continue
            j = css.find('}', i)
            out.append((list(ctx), head, css[i + 1:j]))
            i = j + 1
            continue
        if c == '}':
            if ctx:
                ctx.pop()
            buf = ''
            i += 1
            continue
        buf += c
        i += 1
    return out


def generate(css):
    rules, out = parse(css), []
    for ctx, sel, body in rules:
        if sel.startswith(':root') or 'data-theme' in sel:
            continue
        if sel.startswith('.theme-toggle') or 'masthead__menu #site-nav' in sel:
            continue
        if 'selection' in sel:            # ::selection 在主题文件第 7 节单独处理
            continue
        decls = []
        for d in split_decls(body):
            if ':' not in d:
                continue
            prop, val = [x.strip() for x in d.split(':', 1)]
            if prop.startswith('--'):
                continue
            new, changed = val, False
            for lit in sorted(LITERALS, key=len, reverse=True):
                pat = r'(?<![0-9a-fA-F])' + re.escape(lit) + r'(?![0-9a-fA-F])'
                if re.search(pat, new):
                    tok = pick(prop, sel, lit)
                    if tok:
                        new = re.sub(pat, f'var({tok})', new)
                        changed = True
            if changed:
                decls.append(f'{prop}: {new}')
        if not decls:
            continue
        block = f'{sel} {{ {"; ".join(decls)} }}'
        for at in reversed(ctx):
            block = f'{at} {{\n  {block}\n}}'
        out.append(block)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--baseline', required=True, help='引入主题层之前的 main.css')
    ap.add_argument('--apply', action='store_true', help='写回 _sass/_cosmos-theme.scss 第 3 节')
    ap.add_argument('--theme', default='_sass/_cosmos-theme.scss')
    args = ap.parse_args()

    css = open(args.baseline, encoding='utf-8').read()
    print('=== 基线中的颜色字面值 ===')
    for k, v in Counter(re.findall(r'#[0-9a-fA-F]{3,8}\b', css)).most_common():
        flag = '  <- 已映射' if k.lower() in LITERALS else ''
        print(f'   {v:4}  {k}{flag}')

    rules = generate(css)
    print(f'\n=== 生成 {len(rules)} 条规则 ===')
    for r in rules:
        if r.startswith('@'):
            print(r)

    if not args.apply:
        print('\n（干跑，未写入。加 --apply 写入主题文件第 3 节）')
        return

    text = open(args.theme, encoding='utf-8').read()
    i3 = text.index('   3. MM 组件规则')
    s3 = text.rfind('/* ---', 0, i3)
    i4 = text.index('   4. 顶栏主题切换控件')
    s4 = text.rfind('/* ---', 0, i4)
    head = ('/* --------------------------------------------------------------------------\n'
            '   3. MM 组件规则（由引入主题层之前的 main.css 程序化生成，共 %d 条；\n'
            '      重新生成：python3 theme-rules-gen.py --baseline <旧 main.css> --apply）\n'
            '   -------------------------------------------------------------------------- */\n' % len(rules))
    tail = text[s4:]
    keep = text[text.index('/* 上面 .author__urls', s3):s4] if '/* 上面 .author__urls' in text[s3:s4] else ''
    open(args.theme, 'w', encoding='utf-8').write(text[:s3] + head + '\n'.join(rules) + '\n' + keep + tail)
    print(f'\n已写回 {args.theme}')
    print('提醒：紧跟在规则后面的 .author__urls 重置块必须保留（脚本已原样带过去）。')


if __name__ == '__main__':
    sys.exit(main())
