import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix header height by safely trimming the logo's bounding box using symmetrical negative margins
def fix_desktop_logo(m):
    return """.header-logo {
    height: 140px; /* Large enough to be prominent, small enough to not make header massive */
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
    margin-top: -30px;
    margin-bottom: -30px;
}"""
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*140px;[^}]*\}', fix_desktop_logo, css)

# Mobile logo: height 100px. Target bounding box: 60px. Margin = -20px
css = re.sub(r'\.header-logo\s*\{\s*height:\s*100px\s*!important;\s*\}', '.header-logo {\n        height: 100px !important;\n        margin-top: -20px !important;\n        margin-bottom: -20px !important;\n    }', css)
css = re.sub(r'height:\s*100px\s*!important;', 'height: 100px !important;\n        margin-top: -20px !important;\n        margin-bottom: -20px !important;', css)


# Fix search bar background to match global background
css = css.replace('.mobile-search-bar {\n    display: none;\n    padding: 1.5rem 16px 1rem; /* Added top padding to clear the logo */\n    background: #000000;', 
                 '.mobile-search-bar {\n    display: none;\n    padding: 1.5rem 16px 1rem; /* Added top padding to clear the logo */\n    background-color: var(--clr-background);')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied symmetrical negative margins to reduce header height and updated search bar background.")
