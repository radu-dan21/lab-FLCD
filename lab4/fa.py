from typing import List, Optional, Set, Tuple

from lab4.state import State
from lab4.transformation import Transformation


class FA:
    def __init__(self):
        self.initial_state_labels: Set[str] = set()
        self.state_labels: Set[str] = set()
        self.final_state_labels: Set[str] = set()

        self.alphabet: Set[str] = set()

        self.transformations: Set[Transformation] = set()

        self.__is_deterministic: Optional[bool] = None

    @property
    def is_deterministic(self):
        if self.__is_deterministic is None:
            self.__is_deterministic = self.__compute_if_is_deterministic()
        return self.__is_deterministic

    def __compute_if_is_deterministic(self) -> bool:
        state_label_alphabet_elem_map: Set[Tuple[str, str]] = set()

        for t in self.transformations:
            if (label_element_tuple := (t.initial_label, t.alphabet_element)) in state_label_alphabet_elem_map:
                return False

            state_label_alphabet_elem_map.add(label_element_tuple)

        return True

    def add_state_label(self, state_label: str):
        self.state_labels.add(state_label)

    def add_initial_state_label(self, state_label: str):
        self.initial_state_labels.add(state_label)
        self.add_state_label(state_label)

    def add_final_state_label(self, state_label: str):
        self.final_state_labels.add(state_label)
        self.add_state_label(state_label)

    def add_transformation(self, transformation: Transformation):
        self.add_state_label(transformation.initial_label)
        self.add_state_label(transformation.final_label)
        self.add_alphabet_element(transformation.alphabet_element)
        self.transformations.add(transformation)

    def add_alphabet_element(self, alphabet_element: str):
        self.alphabet.add(alphabet_element)

    def check_string(self, input_string: str):
        string_characters: List[str] = [character for character in input_string]
        current_states = [State(label, '') for label in self.initial_state_labels]

        if any(character not in self.alphabet for character in string_characters):
            return False

        while string_characters and current_states:
            new_states = []
            current_character = string_characters.pop(0)
            for state in current_states:
                possible_transformations = self._get_possible_transformations(state.label, current_character)
                for transformation in possible_transformations:
                    new_states.append(transformation.transform(state))
            current_states = new_states

        return any(state.label in self.final_state_labels for state in current_states)

    def _get_possible_transformations(self, state_label, alphabet_element):
        return [
            t
            for t in self.transformations
            if t.initial_label == state_label and t.alphabet_element == alphabet_element
        ]

    def get_all_possible_final_states(self):
        current_states = [State(label, '') for label in self.initial_state_labels]
        final_states = set()
        while (next_states := self._get_next_possible_states(current_states)) != current_states:
            final_states.update((state for state in next_states if state.label in self.final_state_labels))
            current_states = next_states
        return final_states

    def _get_next_possible_states(self, current_states):
        next_states = []
        for state in current_states:
            next_states_for_current_state = self._get_all_possible_next_states_for_state(state)
            if next_states_for_current_state:
                next_states.extend(next_states_for_current_state)
            else:
                next_states.append(state)
        return next_states

    def _get_all_possible_next_states_for_state(self, state):
        possible_next_states = []
        possible_transformations = [t for t in self.transformations if t.initial_label == state.label]
        for t in possible_transformations:
            possible_next_states.append(State(t.final_label, state.value + t.alphabet_element))
        return possible_next_states
