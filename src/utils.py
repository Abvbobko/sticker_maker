from pathlib import Path

from PIL import ImagePalette, ImageColor, Image

from src.enums import Color


def color_to_number(color: Color) -> int:
    color = ImageColor.getrgb(color.value)
    r, g, b = color

    return (r * 256 * 256) + (g * 256) + b


def get_image_name(image: Image.Image) -> str:
    filepath = Path(image.filename)
    filename = filepath.stem

    return filename
