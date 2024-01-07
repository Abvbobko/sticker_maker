class ImageContainer:
    def __init__(self, image: str):
        self._image = image

    @property
    def image(self):
        return self._image
