import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore .logo as a normal flex item
def restore_logo(m):
    return """.logo {
    font-family: var(--ff-heading);
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--clr-text-primary);
    text-decoration: none;
    display: flex;
    align-items: center; /* Vertically center image and text */
    gap: 0.5rem;
}"""

css = re.sub(r'\.navbar \.logo\s*\{[^}]*z-index:\s*110;\s*\}', restore_logo, css)

# Remove the nav-left padding that we added for absolute positioning
css = re.sub(r'\.nav-left\s*\{[^}]*padding-left:\s*200px;\s*/\*\s*Space[^}]*\}', '.nav-left {\n    display: flex;\n    align-items: center;\n    gap: 1.5rem;\n}', css)
css = re.sub(r'\.nav-left\s*\{[^}]*padding-left:\s*120px;\s*/\*\s*Space[^}]*\}', '.nav-left {\n        gap: 0.5rem;\n    }', css)


# Use symmetrical negative margins on the header logo to shrink its bounding box perfectly
# Desktop logo: height 220px. Target bounding box: 80px. Margin = (220 - 80) / 2 = 70px
def fix_desktop_logo(m):
    return """.header-logo {
    height: 220px;
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
    margin-top: -70px;
    margin-bottom: -70px;
}"""
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*180px;[^}]*\}', fix_desktop_logo, css)

# Mobile logo: height 140px. Target bounding box: 60px. Margin = (140 - 60) / 2 = 40px
css = re.sub(r'height:\s*160px\s*!important;\s*margin-top:\s*-50px\s*!important;\s*margin-bottom:\s*-50px\s*!important;', 'height: 140px !important;\n        margin-top: -40px !important;\n        margin-bottom: -40px !important;', css)
css = re.sub(r'height:\s*140px\s*!important;\s*\}', 'height: 140px !important;\n        margin-top: -40px !important;\n        margin-bottom: -40px !important;\n    }', css)

# Also remove the absolute positioning overrides in mobile queries
css = css.replace('.navbar .logo {\n        top: 5px;\n        left: 1rem;\n    }', '')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied symmetrical negative margins to perfectly align logo and icons.")
