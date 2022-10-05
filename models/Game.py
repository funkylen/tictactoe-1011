from models.Board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 0

    def check_win(self):
        triples = self.board.get_key_triples_set()

        return triples.check_win()

    def make_turn(self, x, y):

        self.board.set0(x, y) if self.turn % 2 else self.board.setX(x, y)

        self.turn += 1
