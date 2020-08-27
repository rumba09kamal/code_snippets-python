import os

from PIL import Image

for file in os.listdir(os.getcwd()):
    if file.endswith(".png"):
        filename, ext = os.path.splitext(file)
        image = Image.open(os.path.join(os.getcwd(), file))
        rgb_image = image.convert("RGB")
        rgb_image.save(filename + ".jpg", "JPEG")
        #  os.remove(os.path.join(os.getcwd(), filename + ".jpg"))
