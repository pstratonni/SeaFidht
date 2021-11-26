from random import randint

from Dot import Dot
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


class AI(Player):
    targets = []

    def add_targets(self, size):
        for i in range(size):
            for j in range(size):
                self.targets.append(Dot(i, j))

    def ask(self):
        idx = randint(0, len(self.targets) - 1)
        dot = self.targets[idx]
        print(f'Ход компьютера({dot.x+1, dot.y+1})')
        self.targets.pop(idx)
        return dot


class User(Player):
    def ask(self):
        while True:
            print("Введите координаты выстрела через пробел (первая номер строки): ")
            try:
                shoot = tuple(map(int, input().split()))
            except ValueError:
                print('Упс. Координаты - это числа, которые вводятся через пробел.\nПопробуй ещё раз')
                continue
            if len(shoot) != 2:
                print('Нужно две координаты')
                continue
            print(shoot)
            return Dot(shoot[0] - 1, shoot[1] - 1)
