import re

filepath = r'c:\Users\Hp User\Desktop\Jashvanth_Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure JavaScript gets an icon if it doesn't have one
html = re.sub(r'<span class="tech-pill">JavaScript</span>', r'<span class="tech-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript"> JavaScript</span>', html)

# Remove the text content inside .tech-pill tags that contain an image,
# and optionally add a title attribute to the span so hovering shows the name.
def clean_pill(match):
    img_tag = match.group(1)
    # Extract alt text to use as title
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    title = alt_match.group(1) if alt_match else ""
    # Return the span with title and just the image
    return f'<span class="tech-pill" title="{title}">{img_tag}</span>'

# Match <span class="tech-pill"><img ...> Text</span>
html = re.sub(r'<span class="tech-pill">(<img[^>]+>)[^<]+</span>', clean_pill, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
