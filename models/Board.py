from models.Cell import Cell
from models.TripleSet import TripleSet


class Board:
    def __init__(self):
        self.board = [[Cell() for _ in range(3)] for _ in range(3)]

    def setX(self, x: int, y: int):
        self.__check_cell(x, y)
        self.board[x - 1][y - 1].set_X()
    
    def set0(self, x: int, y: int):
        self.__check_cell(x, y)
        self.board[x - 1][y - 1].set_0()

    def get_key_triples_set(self) -> TripleSet:
        return TripleSet(
            [self.board[i][i] for i in range(3)], 
            [self.board[::-1][i][i] for i in range(3)],
            *[i for i in self.board],
            *[[i[j] for i in self.board] for j in range(3)] 
        )

    def show_board(self):
        for row_index, row in enumerate(self.board[::-1]):
            print('|'.join(list(map(lambda cell: cell.value, row))), 
            end='\n' + '-'*5 + '\n' if row_index != 2 else '\n')

    def __check_cell(self, x, y):
        if self.board[x - 1][y - 1].value != ' ':
            raise ValueError
