from lab4.constants import CSV_FILE_NAME
from lab4.csv_reader import CSVReader
from lab4.fa import FA


class UI:
    def __init__(self):
        self.csv_reader = CSVReader()
        self.fa: FA = self.csv_reader.run()

    def start(self):
        while True:
            self.print_menu()
            option = self.read_option()
            match option:
                case 0:
                    break
                case 1:
                    for transformation_str_representation in sorted(str(t) for t in self.fa.transformations):
                        print(transformation_str_representation)
                case 2:
                    for state_str_representation in sorted(str(s) for s in self.fa.get_all_possible_final_states()):
                        print(state_str_representation)
                case 3:
                    input_string = self.read_string()
                    print(f'Does {input_string} match?: {self.fa.check_string(input_string)}')
                case _:
                    print("Invalid option!")

    def print_menu(self):
        print(
            f"\nCSV file: {CSV_FILE_NAME}"
            f"\nIs FA deterministic?: {self.fa.is_deterministic}"
            f"\nSet of states: {sorted(self.fa.state_labels)}"
            f"\nSet of initial states: {sorted(self.fa.initial_state_labels)}"
            f"\nSet of final states: {sorted(self.fa.final_state_labels)}"
            f"\nAlphabet: {sorted(self.fa.alphabet)}"
            f"\n"
            f"\nOptions:"
            f"\n0. Exit"
            f"\n1. Show all transitions"
            f"\n2. Show all possible strings that match (if there are infinite possibilities, this will freeze)"
            f"\n3. Check if string matches"
        )

    @staticmethod
    def read_option():
        option = input(f"\nInput your option: ")
        try:
            int_option = int(option)
            return int_option if int_option in [0, 1, 2, 3] else None
        except ValueError:
            return None

    @staticmethod
    def read_string():
        return input("Input your string: ")
