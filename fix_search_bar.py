import re

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix mobile search bar background
css = re.sub(r'\.mobile-search-bar\s*\{([^}]+)background:\s*transparent;', r'.mobile-search-bar {\g<1>background: var(--clr-background);', css)

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed search bar transparent background.")
