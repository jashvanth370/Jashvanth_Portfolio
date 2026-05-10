filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\styles.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('padding: 80px 20px;', 'padding: 40px 20px;', 1)
css = css.replace('font-size: 1.1rem;\n    max-width: 1300px;', 'font-size: 14px;\n    max-width: 1300px;')

addition = '''
.about .about-visual {
    margin-top: 2rem;
    margin-bottom: 2rem;
    height: auto;
}
'''
if ".about .about-visual" not in css:
    css += addition

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)
