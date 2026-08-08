import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Theme Colors
css = re.sub(r'--clr-background:.*?;', '--clr-background: #0B0B0B;', css)
css = re.sub(r'--clr-surface:.*?;', '--clr-surface: #161616;', css)
css = re.sub(r'--clr-surface-dark:.*?;', '--clr-surface-dark: #000000;', css)
css = re.sub(r'--clr-primary:.*?;', '--clr-primary: #D4AF37;', css)
css = re.sub(r'--clr-primary-dark:.*?;', '--clr-primary-dark: #B5952F;', css)
css = re.sub(r'--clr-text-primary:.*?;', '--clr-text-primary: #F5F5F5;', css)
css = re.sub(r'--clr-text-on-dark:.*?;', '--clr-text-on-dark: #000000;', css)
css = re.sub(r'--clr-badge-danger:.*?;', '--clr-badge-danger: #8B0000;', css)
css = re.sub(r'--clr-star:.*?;', '--clr-star: #D4AF37;', css)

# Fix contrast issues on buttons
css = css.replace('color: white;', 'color: var(--clr-text-on-dark);')

# Text colors for dark mode
css = re.sub(r'color:\s*#555(555)?;', 'color: #B0B0B0;', css)
css = re.sub(r'color:\s*#666(666)?;', 'color: #A0A0A0;', css)
css = re.sub(r'color:\s*#888(888)?;', 'color: #888888;', css)

# Backgrounds
css = css.replace('background-color: white;', 'background-color: var(--clr-surface);')
css = css.replace('background: white;', 'background: var(--clr-surface);')
css = css.replace('background-color: #F8F9FA;', 'background-color: #222222;')
css = css.replace('border: 2px solid #E5E5E5;', 'border: 2px solid #444444;')
css = css.replace('border-bottom: 1px solid rgba(0, 0, 0, 0.05);', 'border-bottom: 1px solid rgba(255, 255, 255, 0.05);')
css = css.replace('border-bottom: 1px solid rgba(0,0,0,0.05);', 'border-bottom: 1px solid rgba(255,255,255,0.05);')
css = css.replace('border-top: 1px solid rgba(0,0,0,0.05);', 'border-top: 1px solid rgba(255,255,255,0.05);')
css = css.replace('box-shadow: 0 10px 30px rgba(0,0,0,0.05);', 'box-shadow: 0 10px 30px rgba(0,0,0,0.5);')

# Fix navbar
css = css.replace('background-color: rgba(0, 0, 0, 0.05);', 'background-color: rgba(255, 255, 255, 0.1);')
css = css.replace('background: rgba(0, 0, 0, 0.05);', 'background: rgba(255, 255, 255, 0.1);')

# Header resizing
# Logo Desktop
css = re.sub(r'\.header-logo\s*\{\s*height:\s*\d+px;', '.header-logo {\n    height: 180px;', css)
# Logo Mobile
css = re.sub(r'height:\s*\d+px\s*!important;', 'height: 120px !important;', css)
# Logo very small mobile
css = re.sub(r'\.header-logo\s*\{\s*height:\s*32px;', '.header-logo {\n        height: 80px;', css)

# Reduce header height (Navbar padding)
css = re.sub(r'\.navbar\s*\{[^}]*padding:\s*[0-9.]+rem\s+0;', '.navbar {\n    background-color: var(--clr-background);\n    padding: 0.1rem 0;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css for luxurious theme and header sizes.")
