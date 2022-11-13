import shlex

from functools import reduce
from typing import List, Tuple


OPERATOR_CHARACTERS = ['<', '>', '=', '|', '&', '!', '+', '-', '*', '/', '%']


class Tokenizer:
    def __init__(self, text: str):
        self._text = text
        self._shlex_instance = self._create_shlex_instance()

    def _create_shlex_instance(self):
        return shlex.shlex(
            instream=self._text,
            posix=False,
            punctuation_chars=';' + reduce(lambda a, b: a + b, OPERATOR_CHARACTERS, ''),
        )

    def _get_line_and_token(self):
        line = self._get_line_of_current_token()
        try:
            token = self._shlex_instance.get_token()
        except ValueError:
            raise RuntimeError(f"String that is never closed on line {line}")
        return line, token

    def _get_line_of_current_token(self) -> int:
        # String of the form (without <>): <"Filename", line K: >
        file_and_lineno_string = self._shlex_instance.error_leader()[: -1]
        last_space_index = file_and_lineno_string.rindex(' ')
        return int(file_and_lineno_string[last_space_index + 1: -1])

    def get_tokens(self) -> List[Tuple[int, str]]:
        token_list = []

        tokens = self._get_next_tokens()
        while tokens:
            token_list.extend(tokens)
            tokens = self._get_next_tokens()

        return token_list

    def _check_formatted_string_edge_case(self, tokens):
        next_line, next_token = self._get_line_and_token()
        if next_token.startswith('"'):
            prev_line, prev_token = tokens[0]
            return [(prev_line, prev_token + next_token)]
        return tokens + (next_line, next_token)

    def _check_operator_edge_case(self, tokens):
        prev_line, prev_token = tokens[0]
        next_line, next_token = self._get_line_and_token()
        while next_token in OPERATOR_CHARACTERS:
            prev_token += next_token
            next_line, next_token = self._get_line_and_token()
        return [(prev_line, prev_token), (next_line, next_token)]

    def _get_next_tokens(self) -> List[Tuple[int, str]]:
        line, token = self._get_line_and_token()
        tokens = [(line, token)] if token else []

        if token == '@':
            tokens = self._check_formatted_string_edge_case(tokens)

        elif token in OPERATOR_CHARACTERS:
            tokens = self._check_operator_edge_case(tokens)

        return tokens
