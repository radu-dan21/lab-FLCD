from typing import Optional


class Node:
    __NUMBER_OF_NODES: int = 0

    def __init__(self, token):
        self.__token: str = token
        self.__identifier: int = Node.__NUMBER_OF_NODES
        Node.__NUMBER_OF_NODES += 1
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    @property
    def token(self):
        return self.__token

    @property
    def identifier(self):
        return self.__identifier

    @classmethod
    def get_number_of_nodes(cls):
        return cls.__NUMBER_OF_NODES

    def __eq__(self, other):
        return self.token == other.token

    def __lt__(self, other):
        return self.token < other.token

    def __gt__(self, other):
        return self.token > other.token

    def __str__(self):
        return f'{self.identifier:3d} {self.token:{" "}{"<"}{25}} '
