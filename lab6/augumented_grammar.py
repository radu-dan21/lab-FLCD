from typing import Optional, List

from lab5 import Grammar, GrammarComponent, NonTerminal, Production

from lab6.grammar_components import AugumentedStartingSymbol, Dot


class AugumentedGrammar(Grammar):
    def __init__(self, non_augumented_grammar: Grammar, starting_symbol: NonTerminal):  # noqa
        self._non_augmented_grammar = non_augumented_grammar
        self._starting_symbol = starting_symbol
        super().__init__([])

    def get_augumented_grammar_production(self, production: Production, idx: Optional[int] = None):
        if idx is None:
            idx = 0
        rhs_copy: List[GrammarComponent] = production.rhs.copy()
        rhs_copy.insert(idx, Dot())

        return Production(production.lhs, rhs_copy)

    def process(self) -> List[Production]:
        productions: List[Production] = [
            Production(
                [AugumentedStartingSymbol(self._starting_symbol)],
                [Dot(), self._starting_symbol]
            )
        ]
        for grammar_production in self._non_augmented_grammar.get_productions():
            productions.append(self.get_augumented_grammar_production(grammar_production))

        return productions
