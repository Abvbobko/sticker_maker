from src.image_container import ImageContainer
from src.steps.step import Step


class Pipeline:
    def __init__(self, steps: list[Step]):
        self._steps = steps

    def run(self, image: ImageContainer):
        for step in self._steps:
            image = step.run(image)

        return image
