from PIL import ImagePalette, ImageColor

from src.enums import Color


def color_to_number(color: Color) -> int:
    color = ImageColor.getrgb(color.value)
    return ImagePalette.ImagePalette(mode="RGB").getcolor(color)
