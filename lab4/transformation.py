from lab4.state import State


class Transformation:
    def __init__(self, initial_label, final_label, alphabet_element):
        self.initial_label = initial_label
        self.final_label = final_label
        self.alphabet_element = alphabet_element

    def transform(self, initial_state: State):
        if initial_state.label != self.initial_label:
            return None
        return State(self.final_label, initial_state.value + self.alphabet_element)

    def __str__(self):
        return f'{self.initial_label}, {self.alphabet_element} -> {self.final_label}'

    def __eq__(self, other):
        return (
            isinstance(other, Transformation)
            and other is not None
            and self.initial_label == other.final_label
            and self.alphabet_element == other.alphabet_element
            and self.final_label == other.final_label
        )

    def __hash__(self):
        return hash((self.initial_label, self.final_label, self.alphabet_element))
