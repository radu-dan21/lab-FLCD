from lab5.grammar_components import Terminal


class Dollar(Terminal):
    def __init__(self):
        super().__init__('$')
