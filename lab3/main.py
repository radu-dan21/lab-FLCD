from lab3.controller import Controller
from lab3.file_config import INPUT_FILES_DIR


if __name__ == "__main__":
    FILE_NAMES = INPUT_FILES_DIR.rglob('*')
    controller = Controller(FILE_NAMES)
    controller.run()
