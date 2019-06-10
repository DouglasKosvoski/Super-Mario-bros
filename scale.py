# script used to resize images

from PIL import Image

img = Image.open('image_name_default.png')

new_img = img.resize((30, 30))
new_img.save("new_image_name.png", "PNG", optimize=True)
