from lab5 import Grammar, NonTerminal, print_grammar_info, read_grammar
from lab6.augumented_grammar import AugumentedGrammar


def get_starting_symbol(grammar):
    starting_symbol = NonTerminal(input("Please input the staring symbol: "))
    terminals = grammar.get_non_terminals()
    if starting_symbol not in terminals:
        raise RuntimeError("Starting symbol not in terminals list")
    return starting_symbol


if __name__ == "__main__":
    grammar: Grammar = read_grammar()
    starting_symbol = get_starting_symbol(grammar)
    # print_grammar_info(grammar)

    augumented_grammar = AugumentedGrammar(grammar, starting_symbol)
    augumented_grammar.process()

    print_grammar_info(augumented_grammar)
