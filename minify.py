import re, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract <main>...</main> inner content
main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
section = main_match.group(1).strip()

# 2. Extract popup style + div between </main> and the next <script>
after_main_start = content.find('</main>') + len('</main>')
after_main = content[after_main_start:]
next_script = after_main.find('<script>')
popup_html = after_main[:next_script].strip() if next_script != -1 else ''

# 3. Extract SECOND <script> block (outside </main>)
second_script_match = re.search(r'(<script>.*?</script>)', after_main, re.DOTALL)
second_js = second_script_match.group(1) if second_script_match else ''

# 4. Combine (no duplicate scripts)
out = section + '\n' + popup_html + '\n' + second_js

orig_size = len(out)
script_chars = sum(len(m) for m in re.findall(r'<script>.*?</script>', out, re.DOTALL))
style_chars  = sum(len(m) for m in re.findall(r'<style[^>]*>.*?</style>', out, re.DOTALL))
svg_chars    = sum(len(m) for m in re.findall(r'<svg[^>]*>.*?</svg>', out, re.DOTALL))
print(f'Pre-minify:  {orig_size:,} | scripts={script_chars:,} styles={style_chars:,} svgs={svg_chars:,} other={orig_size-script_chars-style_chars-svg_chars:,}')

# 5. Remove HTML comments
out = re.sub(r'<!--.*?-->', '', out, flags=re.DOTALL)

# 6. Minify CSS inside <style> blocks
def tight_css(m):
    css = m.group(2)
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s*([{};:,>~+!])\s*', r'\1', css)
    css = re.sub(r'\s{2,}', ' ', css)
    css = css.strip()
    return f'<style{m.group(1)}>{css}</style>'
out = re.sub(r'<style([^>]*)>(.*?)</style>', tight_css, out, flags=re.DOTALL)

# 7. Minify JS inside <script> blocks
def minify_js(m):
    js = m.group(1)
    js = re.sub(r'(?m)^\s*//[^\n]*\n', '', js)
    js = re.sub(r'(?<!:)//(?!>)[^\n]*', '', js)
    js = re.sub(r'\n\s*\n+', '\n', js)
    js = re.sub(r'^\s+', '', js, flags=re.MULTILINE)
    return '<script>' + js.strip() + '</script>'
out = re.sub(r'<script>(.*?)</script>', minify_js, out, flags=re.DOTALL)

# 8. Minify SVG whitespace
def minify_svg(m):
    svg = m.group(0)
    svg = re.sub(r'>\s+<', '><', svg)
    svg = re.sub(r'\s{2,}', ' ', svg)
    return svg
out = re.sub(r'<svg[\s\S]*?</svg>', minify_svg, out)

# 9. Collapse whitespace in HTML (outside script/style/svg)
parts = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>|<svg[\s\S]*?</svg>)', out)
final_parts = []
for part in parts:
    if part.startswith(('<script', '<style', '<svg')):
        final_parts.append(part)
    else:
        part = re.sub(r'>\s+<', '><', part)
        part = re.sub(r'\s{2,}', ' ', part)
        final_parts.append(part.strip())
out = ''.join(final_parts)

final_size = len(out)
script_chars2 = sum(len(m) for m in re.findall(r'<script>.*?</script>', out, re.DOTALL))
style_chars2  = sum(len(m) for m in re.findall(r'<style[^>]*>.*?</style>', out, re.DOTALL))
svg_chars2    = sum(len(m) for m in re.findall(r'<svg[^>]*>.*?</svg>', out, re.DOTALL))
print(f'Post-minify: {final_size:,} | scripts={script_chars2:,} styles={style_chars2:,} svgs={svg_chars2:,} other={final_size-script_chars2-style_chars2-svg_chars2:,}')
print(f'Saved: {orig_size - final_size:,} chars')
limit = 63055
diff = final_size - limit
print(f'vs ~63055 limit: {diff:+,} ({"OVER" if diff > 0 else "UNDER"} by {abs(diff):,})')

with open('godaddy_html_section.txt', 'w', encoding='utf-8') as f:
    f.write(out)
print('Written: godaddy_html_section.txt')
