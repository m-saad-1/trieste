import glob
import re

# 1. Update style.css
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Contact section background to match Light Dark
css = css.replace('.contact-section {\n    padding: 6rem 0;\n    background-color: var(--clr-surface);',
                  '.contact-section {\n    padding: 6rem 0;\n    background-color: var(--clr-background);')

# Mobile search bar background to match Light Dark
css = css.replace('.mobile-search-bar {\n    display: none;\n    padding: 1.5rem 16px 1rem;\n    background: transparent;',
                  '.mobile-search-bar {\n    display: none;\n    padding: 1.5rem 16px 1rem;\n    background: var(--clr-background);')
css = re.sub(r'\.mobile-search-bar\s*\{[^}]*background-color:[^;]+;', lambda m: m.group(0).replace(m.group(0).split(':')[-1].strip(), 'var(--clr-background);'), css)


# Form fields to "something like dark" (#1A1A1A) so they stand out against the complete black cards
css = re.sub(r'(input|textarea|select)\s*\{[^}]*background-color:\s*var\(--clr-surface\);', lambda m: m.group(0).replace('var(--clr-surface)', '#1A1A1A'), css)
css = re.sub(r'(input|textarea|select)\s*\{[^}]*background:\s*var\(--clr-surface\);', lambda m: m.group(0).replace('var(--clr-surface)', '#1A1A1A'), css)
# If they are currently black #000000
css = re.sub(r'(input|textarea|select)\s*\{[^}]*background-color:\s*#000000;', lambda m: m.group(0).replace('#000000', '#1A1A1A'), css)

# Make sure inputs are always #1A1A1A
if 'input:focus, textarea:focus' in css:
    css = css.replace('input, textarea, select {\n    width: 100%;\n    padding: 1rem;\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    border-radius: var(--border-radius);\n    font-family: var(--ff-body);\n    font-size: 1rem;\n    transition: var(--transition);\n    background-color: var(--clr-surface);',
                      'input, textarea, select {\n    width: 100%;\n    padding: 1rem;\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    border-radius: var(--border-radius);\n    font-family: var(--ff-body);\n    font-size: 1rem;\n    transition: var(--transition);\n    background-color: #1A1A1A;\n    color: white;')

# Also inject a global input override just in case
css += "\n\n/* Form Fields Fixes */\ninput, textarea, select {\n    background-color: #1A1A1A !important;\n    color: white !important;\n}\n"

# Text outside (and inside) cards that are greyish should be lighter/white
css = re.sub(r'color:\s*#666(666)?;', 'color: #E0E0E0;', css)
css = re.sub(r'color:\s*#777(777)?;', 'color: #E0E0E0;', css)
css = re.sub(r'color:\s*#555(555)?;', 'color: #E0E0E0;', css)
css = re.sub(r'color:\s*#888(888)?;', 'color: #E0E0E0;', css)

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update inline styles in HTML for inputs/selects and text
html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Make inline selects dark
    html = html.replace('background: white;', 'background: #1A1A1A; color: white;')
    html = html.replace('background-color: white;', 'background-color: #1A1A1A; color: white;')
    
    # If there are any texts outside cards with inline styles
    html = re.sub(r'color:\s*#333(333)?;', 'color: white;', html)
    html = re.sub(r'color:\s*#555(555)?;', 'color: white;', html)
    html = re.sub(r'color:\s*#666(666)?;', 'color: white;', html)
    html = re.sub(r'color:\s*#777(777)?;', 'color: white;', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated contact backgrounds, input field backgrounds, and text colors.")
