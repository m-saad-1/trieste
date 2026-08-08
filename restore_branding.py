import glob
import os

print("Re-applying Cafe Trieste branding...")

for path in glob.glob('*.html') + glob.glob('pages/*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('HDM Gourmet', 'Cafe Trieste')
    html = html.replace('Logo.avif', 'logo.avif')
    html = html.replace('Hero.avif', 'hero.avif')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Done rebranding.")
