# script used to resize images

from PIL import Image

img = Image.open('tijolo_padrao.png')

new_img = img.resize((30, 30))
new_img.save("tijolo_padrao_resized.png", "PNG", optimize=True)
