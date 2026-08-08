import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove forced height from navbar so it perfectly fits the flex items
css = re.sub(r'\.navbar\s*\{[^}]*height:\s*80px;[^}]*\}', '.navbar {\n    background-color: var(--clr-background);\n    padding: 0.2rem 0;\n    position: sticky;\n    top: 0;\n    z-index: 100;\n}', css)

# Fix Desktop logo
def fix_desktop_logo(m):
    return """.header-logo {
    height: 140px; /* Large enough to be prominent, small enough to not make header massive */
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
}"""
# Match the current desktop logo which might have negative margins or heights
css = re.sub(r'\.header-logo\s*\{[^}]*max-width:\s*100%;[^}]*\}', fix_desktop_logo, css)

# Fix Mobile logo
css = re.sub(r'\.header-logo\s*\{\s*height:\s*160px\s*!important;\s*margin-top:\s*-50px\s*!important;\s*margin-bottom:\s*-50px\s*!important;\s*\}', '.header-logo {\n        height: 100px !important;\n    }', css)
css = re.sub(r'height:\s*140px\s*!important;\s*margin-top:\s*-40px\s*!important;\s*margin-bottom:\s*-40px\s*!important;', 'height: 100px !important;', css)
css = re.sub(r'height:\s*160px\s*!important;\s*margin-top:\s*-50px\s*!important;\s*margin-bottom:\s*-50px\s*!important;', 'height: 100px !important;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored standard flex alignment with reasonable logo sizes")
