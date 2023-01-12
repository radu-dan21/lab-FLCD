from typing import List

from lab5 import NonTerminal
from lab7.augumented_grammar import AugumentedGrammar
from lab7.augumented_production import AugumentedProduction


def closure(augumented_grammar: AugumentedGrammar, augumented_production: AugumentedProduction):
    closure_items: List[AugumentedProduction] = [augumented_production]
    i: int = 0

    while i < len(closure_items):
        item: AugumentedProduction = closure_items[i]
        if item.is_dot_at_the_end():
            i += 1
            continue
        item_rhs_after_dot = item.get_rhs_after_dot()
        item_after_dot = item_rhs_after_dot[0]
        if isinstance(item_after_dot, NonTerminal):
            for production in augumented_grammar.get_productions_with_non_terminal_lhs(item_after_dot):
                if production not in closure_items:
                    closure_items.append(production)
        i += 1

    return set(closure_items)
