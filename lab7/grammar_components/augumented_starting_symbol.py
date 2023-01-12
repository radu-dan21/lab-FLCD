from lab5 import NonTerminal


class AugumentedStartingSymbol(NonTerminal):
    def __init__(self, starting_symbol: NonTerminal):
        super().__init__(starting_symbol.text + "'")
