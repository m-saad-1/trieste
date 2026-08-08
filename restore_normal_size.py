import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore normal navbar padding
css = re.sub(r'\.navbar\s*\{[^}]*padding:\s*[0-9.]+rem\s+0;[^}]*\}', '.navbar {\n    background-color: var(--clr-background);\n    padding: 0.5rem 0;\n    position: sticky;\n    top: 0;\n    z-index: 100;\n}', css)
css = css.replace('padding: 0;', 'padding: 0.5rem 0;')

# Restore normal desktop logo
def restore_desktop_logo(m):
    return """.header-logo {
    height: 115px;
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
}"""
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*140px;[^}]*\}', restore_desktop_logo, css)

# Restore normal mobile logo
css = re.sub(r'\.header-logo\s*\{\s*height:\s*100px\s*!important;\s*margin-top:\s*-20px\s*!important;\s*margin-bottom:\s*-20px\s*!important;\s*\}', '.header-logo {\n        height: 80px !important;\n    }', css)
css = re.sub(r'height:\s*100px\s*!important;\s*margin-top:\s*-20px\s*!important;\s*margin-bottom:\s*-20px\s*!important;', 'height: 80px !important;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored logo to normal size without negative margins.")
