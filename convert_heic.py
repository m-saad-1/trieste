from PIL import Image
import pillow_avif
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    import os
    os.system("pip install pillow-heif")
    import pillow_heif
    pillow_heif.register_heif_opener()

img = Image.open('assets/images/About.heic')
img.save('assets/images/about.avif', 'AVIF')
print("Converted About.heic to about.avif")
