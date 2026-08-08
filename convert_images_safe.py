import os
import glob
from PIL import Image
import pillow_avif
import time
import gc
import re

def convert_to_avif_safe(directory):
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.JPG', '*.JPEG', '*.PNG', '*.WEBP']
    files_to_convert = []
    
    for ext in extensions:
        files_to_convert.extend(glob.glob(os.path.join(directory, ext)))
            
    files_to_convert = list(set(files_to_convert))
    
    for f in files_to_convert:
        if f.lower().endswith('.avif'):
            continue
            
        if os.path.basename(f).lower() == 'favicon.png':
            print("Skipping favicon.png")
            continue
            
        print(f"Converting: {f}...")
        try:
            img = Image.open(f)
            # Ensure it is converted to RGB if it's RGBA and we are saving to AVIF
            # AVIF supports alpha, but sometimes converting helps avoid errors, let's just let pillow_avif handle it
            avif_path = os.path.splitext(f)[0] + '.avif'
            img.save(avif_path, 'AVIF')
            img.close()
            del img
            gc.collect()
            print(f"Success: {avif_path}")
            os.remove(f)
            print("Waiting 2 seconds to prevent overload...")
            time.sleep(2)
        except Exception as e:
            print(f"Error converting {f}: {e}")

print("Starting safe conversion for all other images...")
convert_to_avif_safe('assets/images')
print("Done converting images.")

print("Updating code references...")
def replace_extensions_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(m):
        return m.group(1) + ".avif"

    # match anything in assets/images except favicon.png
    # Use a function to selectively replace
    def custom_repl(m):
        full_match = m.group(0)
        if 'favicon.png' in full_match.lower():
            return full_match
        return m.group(1) + ".avif"

    new_content = re.sub(r'([\'"\(\s][\.a-zA-Z0-9_/\\-]*?assets/images/[^"\'\)\s]+?)\.(jpg|jpeg|png|webp)', custom_repl, content, flags=re.IGNORECASE)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

files_to_check = glob.glob('*.html') + glob.glob('pages/*.html') + ['assets/css/style.css', 'assets/js/script.js', 'assets/data/menu.json', 'generate_menu.py', 'update_html.py']
for p in files_to_check:
    if os.path.exists(p):
        replace_extensions_in_file(p)

print("Regenerating menu HTML...")
os.system("python generate_menu.py")
os.system("python update_html.py")

print("All done.")
