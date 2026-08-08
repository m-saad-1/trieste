import os
import glob
from PIL import Image
import pillow_avif
import time
import re

def convert_to_avif(directory):
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.JPG', '*.JPEG', '*.PNG', '*.WEBP']
    files_to_convert = []
    
    for ext in extensions:
        files_to_convert.extend(glob.glob(os.path.join(directory, ext)))
            
    files_to_convert = list(set(files_to_convert))
    
    for f in files_to_convert:
        if f.lower().endswith('.avif'):
            continue
            
        print(f"Converting: {f}")
        try:
            with Image.open(f) as img:
                avif_path = os.path.splitext(f)[0] + '.avif'
                img.save(avif_path, 'AVIF')
            print(f"Success: {avif_path}")
            os.remove(f)
            time.sleep(0.5) # prevent overload
        except Exception as e:
            print(f"Error converting {f}: {e}")

print("Starting conversion for gallery...")
convert_to_avif('assets/gallery')
print("Starting conversion for images...")
convert_to_avif('assets/images')
print("Done converting images.")

print("Updating code references...")
def replace_extensions_in_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(m):
        return m.group(1) + ".avif"

    # match anything in assets/images or assets/gallery
    new_content = re.sub(r'([\'"\(\s][\.a-zA-Z0-9_/\\-]*?assets/(?:images|gallery)/[^"\'\)\s]+?)\.(jpg|jpeg|png|webp)', repl, content, flags=re.IGNORECASE)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

files_to_check = glob.glob('*.html') + glob.glob('pages/*.html') + ['assets/data/menu.json', 'assets/css/style.css', 'generate_menu.py', 'assets/js/script.js']
for p in files_to_check:
    if os.path.exists(p):
        replace_extensions_in_file(p)

# We also need to regenerate the menu since menu.json updated
print("Regenerating menu HTML...")
os.system("python generate_menu.py")
os.system("python update_html.py")

print("All done.")
