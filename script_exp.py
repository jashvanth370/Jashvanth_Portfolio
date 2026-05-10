import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Transform Company Name to a link
html = html.replace('<p class="company-name">Boffo System Labs (Pvt) Ltd</p>', '<a href="#" class="company-name" target="_blank" rel="noopener noreferrer" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">Boffo System Labs (Pvt) Ltd <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.8rem;"></i></a>')

# 2. Transform .tech-item into .tech-pill in the Experience section
# It looks like:
# <div class="tech-item">
#     <img src="..."
#         alt="C#" />
#     <span>C#</span>
# </div>

def replace_tech_item(match):
    img_tag = match.group(1).strip()
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    title = alt_match.group(1) if alt_match else ""
    return f'<span class="tech-pill" title="{title}">\n{img_tag}\n</span>'

# We can find all tech-item blocks
pattern = re.compile(r'<div class="tech-item">\s*(<img[^>]+>)\s*<span>[^<]+</span>\s*</div>', re.MULTILINE | re.DOTALL)
html = pattern.sub(replace_tech_item, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
