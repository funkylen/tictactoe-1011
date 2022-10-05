from models.Game import Game


class App:
    def __init__(self):
        self.game = Game()

    def input_coords(self, player):
        try:
            x, y = tuple(map(int, input(f'Игрок {"0" if player else "X"}\nВведите координаты вашего хода: ').split()))

            if not (1 <= x <= 3 and 1 <= y <= 3):
                raise ValueError

        except ValueError:
            print('Введенные данные неверны')
            return False
        return (x, y)
        
    def make_turn(self):
        player = self.game.turn % 2
        coords = self.input_coords(player)
        
        if not coords:
            self.make_turn()
            return

        try:
            self.game.make_turn(*coords)
        except:
            print('Нельзя ходить по уже заполненой клетке')
            self.make_turn()
            return

    def run(self):
        while True:
            win = self.game.check_win()
            if win != 'play':
                break
            self.game.board.show_board()
            self.make_turn()
            

        print(f'Выиграл игрок {win}' if win != 'draw' else 'Ничья')


if __name__ == '__main__':
    app = App()
    app.run()
