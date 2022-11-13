import csv

from typing import List

from lab4.constants import CSV_FILE_NAME
from lab4.fa import FA
from lab4.transformation import Transformation


class CSVReader:
    def __init__(self, csv_file_name: str = CSV_FILE_NAME):
        self.lines: List[List[str]] = []
        self.csv_file_name: str = csv_file_name

        self.fa: FA = FA()

    def run(self) -> FA:
        self.read_lines()
        self.parse_states_section()
        self.parse_transformations()
        return self.fa

    def read_lines(self) -> None:
        with open(self.csv_file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                self.lines.append(line)

    def parse_states_section(self) -> None:
        self.parse_initial_states()
        self.parse_final_states()

    def parse_initial_states(self) -> None:
        while len(row := self.lines[0]) == 2 and row[1] == 'initial':
            initial_state_label = self.lines.pop(0)[0]
            self.fa.add_initial_state_label(initial_state_label)

    def parse_final_states(self) -> None:
        while len(row := self.lines[0]) == 2 and row[1] == 'final':
            final_state_label = self.lines.pop(0)[0]
            self.fa.add_final_state_label(final_state_label)

    def parse_transformations(self):
        for initial_state_label, alphabet_element, final_state_label in self.lines:
            transformation = Transformation(initial_state_label, final_state_label, alphabet_element)
            self.fa.add_transformation(transformation)
