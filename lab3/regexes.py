import re

from functools import reduce


ZERO = r'0'
NON_ZERO_DIGIT = r'[1-9]'
DIGIT = r'[0-9]'
NON_ZERO_NUMBER = rf'{NON_ZERO_DIGIT}{DIGIT}*'
NUMBER = rf'(0|({NON_ZERO_NUMBER}))'

ASCII_NON_CONTROL_CHAR = r'[ -~]'

INT_CONSTANT = NUMBER
FLOAT_CONSTANT = NUMBER + rf'(\.{DIGIT}+)'
BOOL_CONSTANT = r'((true)|(false))'
CHAR_CONSTANT = rf"'{ASCII_NON_CONTROL_CHAR}?'"
STRING_CONSTANT = rf'@?"{ASCII_NON_CONTROL_CHAR}*"'
CONSTANT_REGEX = rf'({INT_CONSTANT})|({FLOAT_CONSTANT})|({BOOL_CONSTANT})|({CHAR_CONSTANT})|({STRING_CONSTANT})'

SEPARATORS = [',', ';', '(', ')', '{', '}', '[', ']']
SEPARATORS_REGEX = reduce(lambda a, b: a + fr'({re.escape(b)})|', SEPARATORS, '')[:-1]

OPERATORS = ['<', '<=', '=', '==', '=/=', '=>', '>', '||', '&&', '!', '+', '-', '*', '/', '%']
OPERATORS_REGEX = reduce(lambda a, b: a + fr'({re.escape(b)})|', OPERATORS, '')[:-1]

IDENTIFIER_REGEX = r'([a-zA-Z][a-zA-Z0-9_]*)'

KEYWORDS = [
    'int',
    'bool',
    'true',
    'false',
    'char',
    'array',
    'if',
    'else',
    'while',
    'read',
    'print',
    'break',
    'continue',
]
KEYWORD_REGEX = reduce(lambda a, b: a + fr'({re.escape(b)})|', KEYWORDS, '')[:-1]


SYMBOL_TABLE_REGEXES = [(CONSTANT_REGEX, 'constant'), (IDENTIFIER_REGEX, 'identifier')]
NON_SYMBOL_TABLE_REGEXES = [(OPERATORS_REGEX, 'operator'), (SEPARATORS_REGEX, 'separator'), (KEYWORD_REGEX, 'keyword')]
