from src.image_container import ImageContainer
from src.steps.step import Step


class SizeChanger(Step):
    def __init__(self, new_width: int, new_height: int):
        self._width = new_width
        self._height = new_height

    def run(self, image: ImageContainer) -> ImageContainer:
        image = image.image
        image = image.resize((self._width, self._height))

        return ImageContainer(image)

