from pathlib import Path

from PIL import ImagePalette, ImageColor, Image

from src.enums import Color


def color_to_number(color: Color) -> int:
    color = ImageColor.getrgb(color.value)

    return ImagePalette.ImagePalette(mode="RGB").getcolor(color)


def get_image_name(image: Image.Image) -> str:
    filepath = Path(image.filename)
    filename = filepath.stem

    return filename
