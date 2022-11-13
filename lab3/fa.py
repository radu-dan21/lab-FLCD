from lab4.csv_reader import CSVReader

FA_CSV_FILES_PATH = './fa_csv_files/'
CONSTANTS_CSV_PATH = FA_CSV_FILES_PATH + '/constants/'


def get_csv_file_path(relative_path: str):
    return FA_CSV_FILES_PATH + relative_path


def get_constants_csv_file_path(relative_path: str):
    return CONSTANTS_CSV_PATH + relative_path


def get_fa(csv_file_path: str):
    return CSVReader(csv_file_path).run()


SYMBOL_TABLE_FA_S = [
    (get_fa(get_constants_csv_file_path('int.csv')), 'integer_constant'),
    (get_fa(get_constants_csv_file_path('bool.csv')), 'boolean_constant'),
    (get_fa(get_constants_csv_file_path('float.csv')), 'float_constant'),
    (get_fa(get_constants_csv_file_path('character.csv')), 'character_constant'),
    (get_fa(get_constants_csv_file_path('string.csv')), 'string_constant'),
    (get_fa(get_csv_file_path('identifier.csv')), 'identifier'),
]

NON_SYMBOL_TABLE_FA_S = [
    (get_fa(get_csv_file_path('keyword.csv')), 'keyword'),
    (get_fa(get_csv_file_path('operator.csv')), 'operator'),
    (get_fa(get_csv_file_path('separator.csv')), 'separator'),
]
