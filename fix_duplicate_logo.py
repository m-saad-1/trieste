import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the .logo class which is globally applying absolute positioning and pulling the footer logo to the top!

css = css.replace('.logo {\n    position: absolute;', '.navbar .logo {\n    position: absolute;')
css = css.replace('.logo {\n        top: 5px;', '.navbar .logo {\n        top: 5px;')

# Ensure .logo itself remains a standard flex container for the footer, etc.
if '.navbar .logo' not in css:
    print("Warning: could not find the exact pattern. Doing a regex replacement.")
    # More robust regex
    css = re.sub(r'\.logo\s*\{\s*position:\s*absolute;', '.navbar .logo {\n    position: absolute;', css)
    css = re.sub(r'\.logo\s*\{\s*top:\s*5px;', '.navbar .logo {\n        top: 5px;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed duplicate logo issue by scoping absolute positioning to the navbar.")
