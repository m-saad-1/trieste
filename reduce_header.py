import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the logo even bigger and apply negative margins to reduce header height
def replace_desktop_logo(m):
    return """.header-logo {
    height: 260px;
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
    margin-top: -90px;
    margin-bottom: -90px;
    transform: translateY(-5px);
}"""

css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*220px;[^}]*transform:\s*translateY\(-5px\);[^}]*\}', replace_desktop_logo, css)

# Update the mobile one at 371
css = css.replace('height: 140px !important;', 'height: 160px !important;\n        margin-top: -50px !important;\n        margin-bottom: -50px !important;')

# Update the mobile one at 785
css = re.sub(r'\.header-logo\s*\{\s*height:\s*220px;\s*\}', '.header-logo {\n        height: 160px !important;\n        margin-top: -50px !important;\n        margin-bottom: -50px !important;\n    }', css)

# Update the one at 1437
css = re.sub(r'\.header-logo\s*\{\s*height:\s*220px;\s*margin-top:\s*-5px;\s*margin-bottom:\s*-15px;\s*\}', '.header-logo {\n        height: 160px !important;\n        margin-top: -50px !important;\n        margin-bottom: -50px !important;\n    }', css)

# Enforce navbar height limits to guarantee a slim header
css = re.sub(r'\.navbar\s*\{[^}]*z-index:\s*100;[^}]*\}', lambda m: m.group(0).replace('padding: 0;', 'padding: 0;\n    height: 70px;\n    display: flex;\n    align-items: center;'), css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated logo sizes and reduced header height.")
