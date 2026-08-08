import re

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Swap Theme Structure: Light Dark Background, Complete Black Cards
css = css.replace('--clr-background: #0B0B0B;', '--clr-background: #1E1E1E;')
css = css.replace('--clr-surface: #161616;', '--clr-surface: #000000;')

# Update any hardcoded dark greys used for surfaces/cards to pure black
css = css.replace('background-color: #161616;', 'background-color: #000000;')
css = css.replace('background: #161616;', 'background: #000000;')
css = css.replace('background-color: #1a1a1a;', 'background-color: #000000;')
css = css.replace('background: #1a1a1a;', 'background: #000000;')
css = css.replace('background-color: #111111;', 'background-color: #000000;')
css = css.replace('background: #111111;', 'background: #000000;')
css = css.replace('background-color: #222222;', 'background-color: #000000;')
css = css.replace('background: #222222;', 'background: #000000;')

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated theme colors for style.css")
