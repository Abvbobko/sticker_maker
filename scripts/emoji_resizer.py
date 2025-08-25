import os
from pathlib import Path

from PIL import Image

def reformat_image(image_path: str, new_width: int, new_height: int) -> None:
    image = Image.open(image_path, 'r')
    width, height = image.size

    if height > width:
        proportion = new_height / height
        height = new_height
        width = int(width * proportion)
    else:
        proportion = new_width / width
        width = new_width
        height = int(height * proportion)

    image = image.resize((width, height))

    bigside = width if width > height else height

    background = Image.new('RGBA', (bigside, bigside), (0, 0, 0, 0))
    offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

    background.paste(image, offset)
    background.save(f"output/{Path(image_path).stem}.png")
    print("Image has been resized !")


for file in os.listdir("to convert"):
    reformat_image(f"vlada.png", 100, 100)
