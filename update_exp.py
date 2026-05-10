import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

new_list = '''<ul class="experience-list"
                    style="margin-top: 20px; margin-left: 20px; color: var(--text-color); line-height: 1.6; opacity: 0.9; font-size: 0.95rem;">
                    <li style="margin-bottom: 10px;">Developed the frontend and backend for a comprehensive <strong>Salon Management Platform</strong> using clean architecture principles.</li>
                    <li style="margin-bottom: 10px;">Implemented robust <strong>Role-Based Access Control (RBAC)</strong> supporting Super Admin, Owner, Branch Manager, Stylist, and Customer roles.</li>
                    <li style="margin-bottom: 10px;">Engineered core engagement features including <strong>"Add to Favorite"</strong> and a dynamic <strong>Rating & Review system</strong> for stylists and services.</li>
                    <li style="margin-bottom: 10px;">Enhanced application <strong>UI/UX</strong> by developing customizable multi-theme options for personalized user experiences.</li>
                    <li>Participated in Agile workflows via daily <strong>Scrum meetings</strong>, utilizing <strong>ClickUp</strong> and <strong>Azure Backlog</strong> for task management.</li>
                </ul>'''

# Replace the existing ul block
pattern = re.compile(r'<ul class="experience-list"[^>]*>.*?</ul>', re.DOTALL)
html = pattern.sub(new_list, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
