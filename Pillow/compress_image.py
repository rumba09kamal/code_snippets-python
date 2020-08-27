import os

from PIL import Image

for file in os.listdir():
    if file.endswith((".png", ".jpg")):
        file_path = os.path.join(os.getcwd(), file)
        image = Image.open(file_path)
        image.save(file, optimize=True, quality=85)
