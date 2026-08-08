import glob
import re

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Favicon replacements
    content = content.replace('href="./assets/images/Logo.avif"', 'href="./assets/images/favicon.png"')
    content = content.replace('href="../assets/images/Logo.avif"', 'href="../assets/images/favicon.png"')

    # Logo replacements
    content = content.replace('src="./assets/images/Logo.avif"', 'src="./assets/images/logo.png"')
    content = content.replace('src="../assets/images/Logo.avif"', 'src="../assets/images/logo.png"')
    
    # Remove greeting (logo text from header)
    content = re.sub(r'<span class="greeting">.*?</span>', '', content)

    # Also remove "Cafe Trieste<span style="color: var(--clr-primary);">.</span>" from footer just in case they meant anywhere the logo appears
    content = content.replace('Cafe Trieste<span style="color: var(--clr-primary);">.</span>', '')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('*.html') + glob.glob('pages/*.html'):
    update_file(file)
print("done")
