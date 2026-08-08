import re

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 'white' backgrounds
css = css.replace('background-color: white;', 'background-color: var(--clr-surface);')
css = css.replace('background: white;', 'background: var(--clr-surface);')

# Add elegant border and adjust shadows for dark mode visibility on cards and hero
# Product Card
css = css.replace('.product-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.05);',
                  '.product-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.5);')

# Product Card Hover Shadow
css = css.replace('box-shadow: 0 20px 40px rgba(0,0,0,0.1);', 'box-shadow: 0 20px 40px rgba(0,0,0,0.6);')

# Mobile Product Card
css = css.replace('.product-card {\n        flex-direction: row;\n        height: 130px;\n        border-radius: 16px;\n        box-shadow: 0 4px 12px rgba(0,0,0,0.05);\n    }',
                  '.product-card {\n        flex-direction: row;\n        height: 130px;\n        border-radius: 16px;\n        border: 1px solid rgba(212, 175, 55, 0.15);\n        box-shadow: 0 4px 12px rgba(0,0,0,0.5);\n    }')

# Hero Image Placeholder
css = css.replace('.hero-image-placeholder {\n    width: 100%;\n    height: 100%;\n    border-radius: var(--border-radius-lg);\n    overflow: hidden;\n    box-shadow: 0 20px 40px rgba(0,0,0,0.1);\n    position: relative;\n}',
                  '.hero-image-placeholder {\n    width: 100%;\n    height: 100%;\n    border-radius: var(--border-radius-lg);\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    overflow: hidden;\n    box-shadow: 0 20px 40px rgba(0,0,0,0.6);\n    position: relative;\n}')

# Offer Card (if any, although product card usually covers it, let's just make sure)
css = css.replace('.offer-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.05);',
                  '.offer-card {\n    background-color: var(--clr-surface);\n    border-radius: var(--border-radius-lg);\n    border: 1px solid rgba(212, 175, 55, 0.15);\n    overflow: hidden;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.5);')


with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Polished dark theme adaptation of HDM Gourmet structural layout")
