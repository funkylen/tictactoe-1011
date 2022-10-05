from collections import Counter
from models.Cell import Cell


class KeyTriple:
    def __init__(self, *triple: Cell):
        if len(triple) != 3:
            raise ValueError
        if tuple(map(lambda val: isinstance(val, Cell), triple)).count(True) != 3:
            raise ValueError

        self.triple = dict(Counter(tuple(map(lambda x: x.value, triple))))

    def check_row(self):
        if self.triple.get('X', 0) == 3:
            return 'X'
        elif self.triple.get('0', 0) == 3:
            return '0'

    def get_empty_cells(self):
        return self.triple.get(' ', 0)
