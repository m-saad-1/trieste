import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Revert .navbar
def fix_navbar(m):
    return """.navbar {
    background-color: var(--clr-background);
    padding: 0;
    position: sticky;
    top: 0;
    z-index: 100;"""

css = re.sub(r'\.navbar\s*\{[^}]*z-index:\s*100;[^}]*\}', fix_navbar, css)

# Revert desktop logo
def fix_desktop_logo(m):
    return """.header-logo {
    height: 180px;
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
    transform: translateY(-5px);
}"""
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*260px;[^}]*\}', fix_desktop_logo, css)

# Revert mobile logo
css = re.sub(r'\.header-logo\s*\{\s*height:\s*160px\s*!important;\s*margin-top:\s*-50px\s*!important;\s*margin-bottom:\s*-50px\s*!important;\s*\}', '.header-logo {\n        height: 120px !important;\n    }', css)
css = re.sub(r'height:\s*160px\s*!important;\s*margin-top:\s*-50px\s*!important;\s*margin-bottom:\s*-50px\s*!important;', 'height: 120px !important;', css)


with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed header styling")
