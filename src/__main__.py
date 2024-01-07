from src.pipeline import Pipeline
from src.steps.ext_converter import ExtConverter
from src.steps.frame_adder import FrameAdder
from src.steps.size_changer import SizeChanger


def main() -> None:
    steps = [
        SizeChanger(),
        FrameAdder(),
        ExtConverter()
    ]
    pipeline = Pipeline(steps)
    pipeline.run()  # todo: add image


if __name__ == "__main__":
    main()
