from lab5 import Production
from lab7.grammar_components.dot import Dot


class AugumentedProduction(Production):
    def get_dot_index(self) -> int:
        try:
            return self._rhs.index(Dot())
        except ValueError:
            return -1

    def get_rhs_after_dot(self):
        return self._rhs[self.get_dot_index() + 1:]

    def get_symbol_after_dot(self):
        return self.get_rhs_after_dot()[0]

    def is_symbol_after_dot(self, symbol):
        return self.get_symbol_after_dot() == symbol

    def is_dot_at_the_end(self) -> bool:
        return self.rhs[-1] == Dot()

    def is_accepted(self, augumented_grammar) -> bool:
        return (
            self.is_dot_at_the_end()
            and len(self.rhs) == 2
            and self.rhs[0] == augumented_grammar.get_starting_symbol()
        )

    def move_dot_to_right(self) -> Production:
        new_rhs = self.rhs.copy()
        current_dot_idx = self.get_dot_index()
        new_rhs[current_dot_idx], new_rhs[current_dot_idx + 1] = new_rhs[current_dot_idx + 1], new_rhs[current_dot_idx]
        return AugumentedProduction(
            self.lhs,
            new_rhs
        )
