import os
from pathlib import Path

from PIL import Image

from src.const import IGNORE_INPUT_FILES, INPUT_DIR, TG_MAX_HEIGHT, TG_MAX_WIDTH, FRAME_SIZE, OUTPUT_DIR
from src.enums import Color, Format
from src.image_container import ImageContainer
from src.pipeline import Pipeline
from src.steps.image_saver import ImageSaver
from src.steps.frame_adder import FrameAdder
from src.steps.size_changer import SizeChanger
from src.utils import get_image_name


def main() -> None:
    pipeline = get_pipeline()

    file_folder = Path(INPUT_DIR).resolve()
    for file in os.listdir(file_folder):
        filepath = Path(file_folder, file)
        if is_image(file):
            image = Image.open(filepath)
            image_name = get_image_name(image)
            image = ImageContainer(image=image, image_name=image_name)
            pipeline.run(image)


def get_pipeline() -> Pipeline:
    steps = [
        SizeChanger(new_width=TG_MAX_WIDTH, new_height=TG_MAX_HEIGHT),
        FrameAdder(color=Color.WHITE, size=FRAME_SIZE),
        ImageSaver(output_dir=OUTPUT_DIR, output_format=Format.PNG)
    ]
    pipeline = Pipeline(steps)

    return pipeline


def is_image(file: str) -> bool:
    return file not in IGNORE_INPUT_FILES


if __name__ == "__main__":
    main()
