import re
import os

with open(r'd:\WEB_DEVELOPMENT\HDM_Gourmet\assets\css\style.css', 'r', encoding='utf-8') as f:
    hdm_css = f.read()

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    trieste_css = f.read()

# Extract Trieste Root
trieste_root_match = re.search(r':root\s*\{[^}]*\}', trieste_css)
if not trieste_root_match:
    print("Could not find Trieste Root!")
    exit(1)
trieste_root = trieste_root_match.group(0)

# Replace HDM root with Trieste root
hdm_css = re.sub(r':root\s*\{[^}]*\}', trieste_root, hdm_css)

# Now, we need to convert hardcoded light theme colors in HDM_Gourmet to use Trieste's dark theme variables.
# This ensures that structurally it's identical to HDM_Gourmet, but visually it's the luxurious dark theme!

replacements = {
    # Backgrounds
    'background: #fff;': 'background: var(--clr-surface);',
    'background-color: #fff;': 'background-color: var(--clr-surface);',
    'background: #f9f9f9;': 'background: var(--clr-surface);',
    'background-color: #f9f9f9;': 'background-color: var(--clr-surface);',
    'background: #eee;': 'background: #1a1a1a;',
    'background-color: #eee;': 'background-color: #1a1a1a;',
    'background: #ddd;': 'background: #222222;',
    'background-color: #ddd;': 'background-color: #222222;',
    'background-color: #F4F4F4;': 'background-color: #1a1a1a;',
    
    # Text colors
    'color: #444;': 'color: #E0E0E0;',
    'color: #999;': 'color: #A0A0A0;',
    'color: #bbb;': 'color: #888888;',
    'color: #ccc;': 'color: #777777;',
    'color: #ddd;': 'color: #666666;',
    'color: #eee;': 'color: #555555;',

    # We shouldn't globally replace 'color: white;' because some things (like badges) NEED to be white.
    # Trieste root defines var(--clr-text-on-dark) as #000000, which means we shouldn't use it for text on dark backgrounds. 
    # Let's keep color: white; as it is, or replace it where appropriate. Actually, #fff text on #0B0B0B is good.
}

for old, new in replacements.items():
    hdm_css = hdm_css.replace(old, new)

# specific hardcoded hex colors
hdm_css = hdm_css.replace('#FFFFFF', 'var(--clr-surface)')
hdm_css = hdm_css.replace('#ffffff', 'var(--clr-surface)')

# The search input wrapper background
hdm_css = hdm_css.replace('.search-input-wrapper {\n    background-color: #F4F4F4;', '.search-input-wrapper {\n    background-color: #1a1a1a;')

# Footer dark matching
hdm_css = hdm_css.replace('.footer {\n    background-color: #1E1E1E;', '.footer {\n    background-color: #050505;')

# Inputs
hdm_css = re.sub(r'(input|textarea|select)\s*\{[^}]*background-color:\s*#f4f4f4;', lambda m: m.group(0).replace('#f4f4f4', 'var(--clr-surface)'), hdm_css)
hdm_css = re.sub(r'(input|textarea|select)\s*\{[^}]*background:\s*#f4f4f4;', lambda m: m.group(0).replace('#f4f4f4', 'var(--clr-surface)'), hdm_css)

# Borders - Instead of removing them, just make them elegant dark/gold borders
hdm_css = hdm_css.replace('border: 1px solid #E5E5E5;', 'border: 1px solid rgba(212, 175, 55, 0.15);')
hdm_css = hdm_css.replace('border: 1px solid #e5e5e5;', 'border: 1px solid rgba(212, 175, 55, 0.15);')
hdm_css = hdm_css.replace('border: 1px solid #ddd;', 'border: 1px solid rgba(212, 175, 55, 0.15);')
hdm_css = hdm_css.replace('border: 1px solid #eee;', 'border: 1px solid rgba(212, 175, 55, 0.15);')
hdm_css = hdm_css.replace('border-bottom: 1px solid #eee;', 'border-bottom: 1px solid rgba(255, 255, 255, 0.05);')
hdm_css = hdm_css.replace('border-color: #e5e5e5;', 'border-color: rgba(212, 175, 55, 0.15);')

# Now write this perfect CSS back to Cafe_Trieste
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(hdm_css)

print("Successfully merged structural styling from HDM_Gourmet with the deep dark theme of Cafe Trieste.")
