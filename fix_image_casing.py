import glob
import re

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix lowercase logo and hero paths to match the uppercase Git-tracked files
    html = html.replace('logo.avif', 'Logo.avif')
    html = html.replace('hero.avif', 'Hero.avif')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated HTML files to match case-sensitive git filenames.")
