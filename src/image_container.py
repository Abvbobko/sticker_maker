from PIL import Image


class ImageContainer:
    def __init__(
        self,
        image: Image.Image,
        image_name: str
    ):
        self._image = image
        self._name = image_name

    @property
    def image(self) -> Image.Image:
        return self._image

    @property
    def name(self) -> str:
        return self._name
