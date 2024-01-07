from PIL import Image


class ImageContainer:
    def __init__(self, image: Image):
        self._image = image

    @property
    def image(self) -> Image:
        return self._image
