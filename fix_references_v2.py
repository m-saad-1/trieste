import os
import glob
import re

print("Updating code references properly...")

def replace_extensions_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    def custom_repl(m):
        full_match = m.group(0)
        if 'favicon.png' in full_match.lower():
            return full_match
        return m.group(1) + ".avif"

    # Match anything starting with assets/images/ or assets/gallery/ and ending with the target extensions.
    # We use [^\'\"\)\n]+? to match the filename, allowing spaces.
    new_content = re.sub(r'([\'"\(\s][\.a-zA-Z0-9_/\\-]*?assets/(?:images|gallery)/[^\'\"\)\n]+?)\.(jpg|jpeg|png|webp)', custom_repl, content, flags=re.IGNORECASE)

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
