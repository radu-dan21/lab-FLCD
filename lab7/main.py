import functools

from collections import OrderedDict
from typing import List, Optional, Set, Tuple

from lab5 import Grammar, GrammarComponent, NonTerminal, read_grammar
from lab7.augumented_grammar import AugumentedGrammar
from lab7.augumented_production import AugumentedProduction
from lab7.closure import closure
from lab7.grammar_components import Dollar


def get_starting_symbol(grammar):
    starting_symbol = NonTerminal(input("Please input the staring symbol: "))
    non_terminals = grammar.get_non_terminals()
    if starting_symbol not in non_terminals:
        raise RuntimeError("Starting symbol not in non terminals list")
    return starting_symbol


def get_possible_next_symbols(item_set: Set[AugumentedProduction]) -> List[GrammarComponent]:
    return list({
        production.get_symbol_after_dot()
        for production in item_set
        if not production.is_dot_at_the_end()
    })


def compute_item_sets_and_table(augumented_grammar: AugumentedGrammar):
    grammar_components: List[GrammarComponent] = functools.reduce(
        lambda a, b: a + list(b),
        (augumented_grammar.get_terminals(), augumented_grammar.get_non_terminals()),
        [],
    )

    def dict_with_gc_as_keys() -> OrderedDict[GrammarComponent, Optional[int]]:
        d = OrderedDict()
        for gc in grammar_components:
            d[gc] = None
        return d

    item_sets = [closure(augumented_grammar, augumented_grammar.productions[0])]

    item_set_table: List[OrderedDict[GrammarComponent, Optional[int]]] = [dict_with_gc_as_keys()]
    exists_in_item_set: bool
    i = 0

    while i < len(item_sets):
        current_item_set = item_sets[i]
        possible_next_symbols: List[GrammarComponent] = get_possible_next_symbols(current_item_set)
        for symbol in possible_next_symbols:
            corresponding_productions = list(filter(
                lambda p: not p.is_dot_at_the_end() and p.is_symbol_after_dot(symbol),
                current_item_set,
            ))
            new_item_set = set()
            for production in corresponding_productions:
                new_item_set.update(closure(augumented_grammar, production.move_dot_to_right()))

            existing_item_set = -1
            for idx, item_set in enumerate(item_sets):
                if all(production in item_set for production in new_item_set):
                    existing_item_set = idx
                    break

            if existing_item_set != -1:
                item_set_table[i][symbol] = existing_item_set
            else:
                item_sets.append(new_item_set)
                item_set_table.append(dict_with_gc_as_keys())
                item_set_table[i][symbol] = len(item_sets) - 1
        i += 1
    return item_sets, item_set_table


def compute_action_and_goto_tables(
    item_sets: List[Set[AugumentedProduction]],
    item_set_table: List[OrderedDict[GrammarComponent, Optional[int]]],
    grammar: Grammar
) -> Tuple[List[OrderedDict[GrammarComponent, Optional[str]]], List[OrderedDict[GrammarComponent, Optional[str]]]]:
    def dict_with_passed_gc_as_keys(gc_list: Set[GrammarComponent]) -> OrderedDict[GrammarComponent, Optional[str]]:
        d = OrderedDict()
        for gc in gc_list:
            d[gc] = None
        return d
    pass

    action_table: List[OrderedDict[GrammarComponent, Optional[str]]]
    goto_table: List[OrderedDict[GrammarComponent, Optional[str]]]

    grammar_productions = grammar.process()

    action_table_components = grammar.get_terminals()
    action_table_components.add(Dollar())
    action_table = [dict_with_passed_gc_as_keys(action_table_components) for _ in range(len(item_sets))]

    goto_table_components = grammar.get_non_terminals()
    goto_table = [dict_with_passed_gc_as_keys(goto_table_components) for _ in range(len(item_sets))]

    for idx, table_row in enumerate(item_set_table):
        for non_terminal in goto_table_components:
            goto_table[idx][non_terminal] = str(item_set_table[idx][non_terminal])

    # TODO: implement the action table part

    return action_table, goto_table


def main():
    grammar: Grammar = read_grammar()
    starting_symbol = get_starting_symbol(grammar)

    augumented_grammar = AugumentedGrammar(grammar, starting_symbol)
    augumented_grammar.process()

    item_sets, item_set_table = compute_item_sets_and_table(augumented_grammar)

    print(functools.reduce(lambda a, b: a + str(b).ljust(6) + " ", item_set_table[0].keys(), 'idx'.ljust(6) + ' -> '))
    for idx, row in enumerate(item_set_table):
        print(f'{str(idx).ljust(6)} -> {functools.reduce(lambda a, b: a + str(b).ljust(6) + " ", row.values(), "")}')

    print('-' * 100)
    for idx, item_set in enumerate(item_sets):
        print(f"Item set {idx}")
        for item in item_set:
            print(str(item).ljust(6))
        print('-' * 100)

    action_table, goto_table = compute_action_and_goto_tables(item_sets, item_set_table, grammar)

    for row in goto_table:
        for value in row.values():
            print(f'{value} ')


if __name__ == "__main__":
    main()
