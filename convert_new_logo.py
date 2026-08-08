from PIL import Image
import pillow_avif
import os

img = Image.open('assets/images/Logo.png')
img.save('assets/images/logo.avif', 'AVIF')
print("Converted Logo.png to logo.avif")
