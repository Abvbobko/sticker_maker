from PIL import ImageOps

from src.enums import Color
from src.image_container import ImageContainer
from src.steps.step import Step
from src.utils import color_to_number


class FrameAdder(Step):
    def __init__(self, color: Color, size: int):
        self._color = color_to_number(color)
        self._border = size

    def run(self, image: ImageContainer) -> ImageContainer:
        image_name = image.name
        image = image.image
        image = ImageOps.expand(image, border=self._border, fill=self._color)

        return ImageContainer(image=image, image_name=image_name)
