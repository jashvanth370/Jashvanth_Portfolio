import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace jwt.io icon with wikimedia transparent SVG
html = html.replace('https://jwt.io/img/icon.svg', 'https://upload.wikimedia.org/wikipedia/commons/1/1d/JWT_LOGO.svg')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
