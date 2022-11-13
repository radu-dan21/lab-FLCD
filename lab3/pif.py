from typing import List, Tuple


PIFElem = Tuple[str, int, str]


class PIF:

    def __init__(self):
        self.__list: List[PIFElem] = []

    def insert(self, pif_elem: PIFElem):
        self.__list.append(pif_elem)

    def __str__(self):
        str_representation = ''
        for token, position, label in self.__list:
            str_representation += f'{token:{" "}{">"}{50}} {position:3d} {label:{" "}{"<"}{10}}\n'
        return str_representation
