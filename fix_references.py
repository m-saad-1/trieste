import os
import glob
import re

print("Updating code references for filenames with spaces...")
def replace_extensions_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous regex failed because of [^"'\)\s]. 
    # Let's match anything that starts with assets/images/ or assets/gallery/ and ends with .jpg/.png/.webp inside quotes.
    # We can just match .jpg, .png, .jpeg, .webp globally and if they are preceded by assets/images/ or assets/gallery/, replace them.
    
    # Let's use a simpler approach.
    def custom_repl(m):
        full_match = m.group(0)
        if 'favicon.png' in full_match.lower():
            return full_match
        return m.group(1) + ".avif" + m.group(3)

    # Match: (quote)(...assets/images/ or assets/gallery/...)(.jpg)(quote)
    new_content = re.sub(r'([\'"])(.*?assets/(?:images|gallery)/.*?)\.(jpg|jpeg|png|webp)([\'"])', custom_repl, content, flags=re.IGNORECASE)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

files_to_check = glob.glob('*.html') + glob.glob('pages/*.html') + ['assets/css/style.css', 'assets/js/script.js', 'assets/data/menu.json']
for p in files_to_check:
    if os.path.exists(p):
        replace_extensions_in_file(p)

print("Regenerating menu HTML...")
os.system("python generate_menu.py")
os.system("python update_html.py")

print("All done.")
