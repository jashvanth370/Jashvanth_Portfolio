import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'https://img.icons8.com/color/48/json-web-token.png': 'https://jwt.io/img/icon.svg',
    'https://img.icons8.com/color/48/entity-framework.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg',
    'https://img.icons8.com/color/48/bcrypt.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg',
    'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-plain.svg': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg'
}

for old, new in replacements.items():
    html = html.replace(old, new)

addition = '''                    <div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap"><span>Bootstrap</span></div>
                    <div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg" alt="Entity Framework"><span>Entity Framework</span></div>
                    <div class="tech-box"><img src="https://jwt.io/img/icon.svg" alt="JWT"><span>JWT</span></div>'''

search_str = '<div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React Native"><span>React Native</span></div>\n                </div>'
replace_str = f'<div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React Native"><span>React Native</span></div>\n{addition}\n                </div>'
html = html.replace(search_str, replace_str)

addition_tools = '''                    <div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" alt="Bcrypt"><span>Bcrypt</span></div>'''
search_str2 = '<div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original.svg" alt="Microsoft Azure"><span>Microsoft Azure</span></div>\n                </div>'
replace_str2 = f'<div class="tech-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original.svg" alt="Microsoft Azure"><span>Microsoft Azure</span></div>\n{addition_tools}\n                </div>'
html = html.replace(search_str2, replace_str2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
