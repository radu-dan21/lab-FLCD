class State:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, State)
            and other is not None
            and self.label == other.label
            and self.value == other.value
        )

    def __str__(self):
        return f'{self.label}; {self.value}'

    def __hash__(self):
        return hash((self.label, self.value))
