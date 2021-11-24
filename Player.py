from MyException import *


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shoot(target)
                return repeat
            except (RepeatBordException, BoardOutException) as e:
                print(e)
