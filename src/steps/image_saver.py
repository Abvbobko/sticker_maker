from pathlib import Path

from src.enums import Format
from src.image_container import ImageContainer
from src.steps.step import Step
from src.utils import get_image_name


class ImageSaver(Step):
    def __init__(self, output_dir: Path,  output_format: Format):
        self._output_dir = output_dir
        self._format = output_format

    def run(self, image: ImageContainer) -> ImageContainer:
        image_name = image.name
        image = image.image

        image_name = self._add_ext(image_name)
        image_path = Path(self._output_dir, image_name)

        image.save(str(image_path), self._format.value)

        return ImageContainer(image=image, image_name=image_name)

    def _add_ext(self, filename: str) -> str:
        ext = self._format.value.lower()
        if not filename.endswith("."):
            ext = "." + ext

        return filename + ext
