from src.enums import Color
from src.image_container import ImageContainer
from src.steps.step import Step


class FrameAdder(Step):
    def __init__(self, color: Color):
        self._color = color

    def run(self, image: ImageContainer) -> ImageContainer:
        return image
