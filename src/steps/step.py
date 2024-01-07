import abc

from src.image_container import ImageContainer


class Step(abc.ABC):
    @abc.abstractmethod
    def run(self, image: ImageContainer) -> ImageContainer:
        raise NotImplementedError
