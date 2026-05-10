filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\styles.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace padding: 3rem; in .about-content
css = css.replace('padding: 3rem;\n    border-radius: 24px;', 'padding: 2rem;\n    border-radius: 24px;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)
