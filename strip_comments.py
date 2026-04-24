import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

orig = len(content)

# Remove HTML comments
content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

# Remove CSS /* */ comments inside <style> blocks
content = re.sub(
    r'(<style[^>]*>)(.*?)(</style>)',
    lambda m: m.group(1) + re.sub(r'/\*.*?\*/', '', m.group(2), flags=re.DOTALL) + m.group(3),
    content, flags=re.DOTALL)

# Remove JS // comments inside <script> blocks (preserve URLs like https://)
content = re.sub(
    r'(<script[^>]*>)(.*?)(</script>)',
    lambda m: m.group(1) + re.sub(r'(?m)(?<!:)//[^\n]*', '', m.group(2)) + m.group(3),
    content, flags=re.DOTALL)

print(f'Before: {orig:,}  After: {len(content):,}  Saved: {orig - len(content):,}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
