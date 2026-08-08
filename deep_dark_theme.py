import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Enlarge Header Logo More and Reduce Height
css = re.sub(r'\.header-logo\s*\{\s*height:\s*180px;', '.header-logo {\n    height: 220px;', css)
css = css.replace('height: 120px !important;', 'height: 140px !important;')
# For small mobile logo
css = re.sub(r'\.header-logo\s*\{\s*height:\s*80px;', '.header-logo {\n        height: 100px;', css)

# Reduce height
css = re.sub(r'\.navbar\s*\{[^}]*padding:\s*0\.1rem\s+0;', '.navbar {\n    background-color: var(--clr-background);\n    padding: 0;', css)
css = css.replace('padding: 0.1rem 0;', 'padding: 0;')

# 2. Search Bar Background
css = css.replace('.mobile-search-bar {\n    background-color: var(--clr-surface);', '.mobile-search-bar {\n    background-color: #000000;')
css = re.sub(r'\.mobile-search-bar\s*\{[^}]*background-color:[^;]+;', lambda m: m.group(0).replace(m.group(0).split(':')[-1].strip(), '#000000;'), css)

# 3. Fix Hardcoded Light Theme Colors in Backgrounds and Borders
replacements = {
    'background: #fff;': 'background: var(--clr-surface);',
    'background-color: #fff;': 'background-color: var(--clr-surface);',
    'background: #f9f9f9;': 'background: #111111;',
    'background-color: #f9f9f9;': 'background-color: #111111;',
    'background: #eee;': 'background: #1a1a1a;',
    'background-color: #eee;': 'background-color: #1a1a1a;',
    'background: #ddd;': 'background: #222222;',
    'background-color: #ddd;': 'background-color: #222222;',
    'background-color: #F4F4F4;': 'background-color: #1a1a1a;',
    
    # Borders
    'border: 1px solid #E5E5E5;': 'border: 1px solid #333333;',
    'border: 1px solid #e5e5e5;': 'border: 1px solid #333333;',
    'border: 1px solid #ddd;': 'border: 1px solid #444444;',
    'border: 1px solid #eee;': 'border: 1px solid #2a2a2a;',
    'border-color: #e5e5e5;': 'border-color: #333333;',
    'border-bottom: 1px solid #eee;': 'border-bottom: 1px solid #2a2a2a;',
    
    # Text colors
    'color: #444;': 'color: #E0E0E0;',
    'color: #999;': 'color: #A0A0A0;',
    'color: #bbb;': 'color: #888888;',
    'color: #ccc;': 'color: #777777;',
    'color: #ddd;': 'color: #666666;',
    'color: #eee;': 'color: #555555;',
}

for old, new in replacements.items():
    css = css.replace(old, new)

# 4. Form inputs, Profile cards, Order items, etc.
# Some might not have exactly matched the above, let's use regex for specific components if needed
# Actually, the above replacements cover most of `#fff` and `#eee`. Let's also check for `#FFFFFF` and `#ffffff`
css = css.replace('#FFFFFF', 'var(--clr-surface)')
css = css.replace('#ffffff', 'var(--clr-surface)')

# Search Input Wrapper
css = css.replace('.search-input-wrapper {\n    background-color: #F4F4F4;', '.search-input-wrapper {\n    background-color: #1a1a1a;')

# Footer adjustments (ensure it matches the theme)
css = css.replace('.footer {\n    background-color: var(--clr-surface-dark);', '.footer {\n    background-color: #050505;')
css = css.replace('.footer {\n    background-color: #1E1E1E;', '.footer {\n    background-color: #050505;')
css = css.replace('border-top: 1px solid rgba(255, 255, 255, 0.1);', 'border-top: 1px solid rgba(255, 255, 255, 0.05);')

# Let's fix input fields
css = re.sub(r'(input|textarea|select)\s*\{[^}]*background-color:\s*#[a-fA-F0-9]+;', lambda m: m.group(0).replace(m.group(0).split(':')[-1].strip(), 'var(--clr-surface);'), css)

# Make sure to write it back
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied deep dark theme fixes")
