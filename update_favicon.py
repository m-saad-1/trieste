import glob

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # If it's in the root folder (index.html)
    if 'href="./assets/images/Logo.avif"' in html and 'rel="icon"' in html:
        html = html.replace('<link rel="icon" type="image/png" href="./assets/images/Logo.avif">',
                            '<link rel="icon" type="image/png" href="./assets/images/favicon.png">')
    # If it's in the pages/ folder
    if 'href="../assets/images/Logo.avif"' in html and 'rel="icon"' in html:
        html = html.replace('<link rel="icon" type="image/png" href="../assets/images/Logo.avif">',
                            '<link rel="icon" type="image/png" href="../assets/images/favicon.png">')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Favicon references updated successfully.")
