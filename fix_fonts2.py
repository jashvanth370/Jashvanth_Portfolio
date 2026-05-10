import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace font-size: 11px; with font-size: 10px;
html = html.replace('font-size: 11px;', 'font-size: 10px;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
