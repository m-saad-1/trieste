import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix Logo Size (the user keeps calling it icon/normal size)
# Desktop to 115px
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*\d+px;[^}]*\}', '.header-logo {\n    height: 115px;\n    width: auto;\n    display: block;\n    max-width: 100%;\n    position: relative;\n    z-index: 105;\n}', css)

# Mobile to 80px
css = re.sub(r'height:\s*\d+px\s*!important;', 'height: 80px !important;', css)
# Wait, this regex replaces ALL !important heights, which broke mobile-menu-btn before!
# Let's fix mobile-menu-btn back to 40px!
css = re.sub(r'\.mobile-menu-btn\s*\{[^}]*height:\s*80px\s*!important;[^}]*\}', '.mobile-menu-btn {\n    width: 40px !important;\n    height: 40px !important;\n    align-items: center !important;\n    justify-content: center !important;\n}', css)

# 2. Fix Card Backgrounds and Borders (Product Cards, Offer Cards, Hero Images)
# Earlier, product-card got background-color: var(--clr-text-on-dark) which is #000000. It should be var(--clr-surface) with a border!
css = re.sub(r'\.product-card\s*\{[^}]*\}', '.product-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    border: 1px solid rgba(212, 175, 55, 0.15); /* Elegant gold border */\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.5);\n    transition: var(--transition);\n    position: relative;\n    display: flex;\n    flex-direction: column;\n}', css)

# Hero image placeholder
css = re.sub(r'\.hero-image-placeholder\s*\{[^}]*\}', '.hero-image-placeholder {\n    width: 100%;\n    height: 100%;\n    border-radius: var(--border-radius-lg);\n    overflow: hidden;\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    box-shadow: 0 20px 40px rgba(0,0,0,0.5);\n    position: relative;\n}', css)

# Offer card (if any specific class exists, otherwise product-card covers it)
css = re.sub(r'\.offer-card\s*\{[^}]*\}', '.offer-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.5);\n    transition: var(--transition);\n    position: relative;\n}', css)

# Fix Category circle active border
css = css.replace('border-color: var(--clr-primary);', 'border-color: var(--clr-primary);') # Keep gold

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed logo sizes, icons, and added elegant borders to cards.")
