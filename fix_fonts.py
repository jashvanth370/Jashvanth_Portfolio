import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace font-size: 0.95rem; with font-size: 11px;
html = html.replace('font-size: 0.95rem;', 'font-size: 11px;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
