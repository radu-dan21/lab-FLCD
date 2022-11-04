from typing import Optional

from node import Node


class SymbolTable:
    def __init__(self):
        self.__root: Optional[Node] = None

    def insert(self, token: str) -> int:
        node: Node = Node(token)

        if self.__root is None:
            self.__root = node
        else:
            self._insert_recursive(self.__root, node)

        return node.identifier

    def _insert_recursive(self, current_node: Node, node_to_insert: Node) -> None:
        if node_to_insert < current_node:
            if current_node.left is None:
                current_node.left = node_to_insert
            else:
                self._insert_recursive(current_node.left, node_to_insert)
        elif node_to_insert > current_node:
            if current_node.right is None:
                current_node.right = node_to_insert
            else:
                self._insert_recursive(current_node.right, node_to_insert)
        else:
            raise RuntimeError(f"{current_node.token} already exists in ST!")

    def contains(self, token: str) -> int:
        # returns -1 if node does not exists, else returns its identifier (int, position)
        return self._contains_recursive(self.__root, token)

    def _contains_recursive(self, current_node: Node, token: str) -> int:
        if current_node is None:
            return -1
        if current_node.token == token:
            return current_node.identifier

        if token < current_node.token:
            return self._contains_recursive(current_node.left, token)
        return self._contains_recursive(current_node.right, token)

    def get_nodes_list(self):
        return self._get_nodes_recursive(self.__root)

    def _get_nodes_recursive(self, node):
        if node is None:
            return []

        lst = []
        lst += self._get_nodes_recursive(node.left)
        lst.append(node)
        lst += self._get_nodes_recursive(node.right)

        return lst

    def __str__(self):
        str_representation = ''
        for node in self.get_nodes_list():
            str_representation += f'{node}\n'
        return str_representation
