from pathlib import Path

PROJECT_ROOT = Path('.').absolute()
FILES_ROOT = PROJECT_ROOT.joinpath('files')

INPUT_FILES_DIR = FILES_ROOT.joinpath('input')
OUTPUT_FILES_DIR = FILES_ROOT.joinpath('output')

ST_FILES_DIR = OUTPUT_FILES_DIR.joinpath('st')
PIF_FILES_DIR = OUTPUT_FILES_DIR.joinpath('pif')
