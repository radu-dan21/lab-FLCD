import re

from lab3.file_config import PIF_FILES_DIR, ST_FILES_DIR
from lab3.pif import PIF
from lab3.regexes import NON_SYMBOL_TABLE_REGEXES, SYMBOL_TABLE_REGEXES
from lab3.symbol_table import SymbolTable
from lab3.tokenizer import Tokenizer


class Controller:
    def __init__(self, file_paths: list):
        self._file_names = file_paths

    def run(self):
        for file_path in self._file_names:
            try:
                text = file_path.read_text()
            except FileNotFoundError as _:
                print(f"\nInvalid file path: {file_path}!\n")
                continue

            file_name = file_path.parts[-1]

            try:
                self._save_pif_and_st(file_name, *self._get_pif_and_st(text))
                print(f'File {file_name} is lexically correct!\n')
            except Exception as e:
                print(f'\nFile {file_name} is NOT lexically correct! {e}\n')

    @staticmethod
    def _save_pif_and_st(file_name, pif, st):
        PIF_FILES_DIR.joinpath(f'{file_name}_pif').write_text(str(pif))
        ST_FILES_DIR.joinpath(f'{file_name}_st').write_text(str(st))
        print(f'\nSaved PIF and ST for {file_name}!')

    @staticmethod
    def _get_pif_and_st(text):
        pif = PIF()
        st = SymbolTable()

        tokenizer = Tokenizer(text)

        for line, token in tokenizer.get_tokens():
            matched = False

            for regex, pif_label in NON_SYMBOL_TABLE_REGEXES:
                if re.fullmatch(regex, token):
                    matched = True
                    pif.insert((token, -1, pif_label))
                    break

            for regex, pif_label in SYMBOL_TABLE_REGEXES:
                if re.fullmatch(regex, token):
                    if not matched:
                        matched = True
                        position = st.insert(token) if (st_id := st.contains(token)) == -1 else st_id
                        pif.insert((token, position, pif_label))

            if not matched:
                raise RuntimeError(f"Invalid token: {token} on line {line}!")

        return pif, st
