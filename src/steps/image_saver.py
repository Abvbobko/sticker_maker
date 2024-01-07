from src.enums import Format
from src.image_container import ImageContainer
from src.steps.step import Step


class ImageSaver(Step):
    def __init__(self, output_dir: str,  output_format: Format):  # todo: change to Path
        # todo: ext to enum
        self._output_dir = output_dir
        self._format = output_format

    def run(self, image: ImageContainer) -> ImageContainer:
        image = image.image
        # todo: combine image name + dir
        image.save(self._output_dir, self._format)

        return ImageContainer(image)
