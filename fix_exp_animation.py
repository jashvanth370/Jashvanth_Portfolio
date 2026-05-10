filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\styles.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

addition = '''
/* Disable animation for tech pills in experience section */
.experience .tech-pill:hover {
    transform: none;
    box-shadow: none;
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(var(--primary-rgb), 0.2);
    cursor: default;
}
'''
if "Disable animation for tech pills in experience section" not in css:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(addition)
