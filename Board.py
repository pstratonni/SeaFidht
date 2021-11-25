from Dot import Dot
from MyException import *


class Board:
    def __init__(self, hid=False, size=6):
        self.board = [['-'] * size for i in range(size)]
        self.hid = hid
        self.size = size
        self.count = 0
        self.busy = []
        self.ships = []

    def __str__(self):
        field = ""
        field += f'  |\t'
        for i in range(self.size):
            field += f'{i + 1} |\t'
        field += '\n'
        for i in range(self.size):
            field += f'{i + 1} |\t'
            for j in range(self.size):
                field += f'{self.board[i][j]} |\t'
            field += '\n'
        if self.hid:
            field = field.replace('■', '-')
        return field

    def contour(self, ship, verb=False):
        for d in ship.dots:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dot = Dot(d.x + i, d.y + j)
                    if not self.out_field(dot.x, dot.y) and dot not in self.busy:
                        if verb:
                            self.board[dot.x][dot.y] = "T"
                        self.busy.append(dot)

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out_field(dot.x, dot.y) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.board[dot.x][dot.y] = '■'
            self.busy.append(dot)
        self.ships.append(ship)
        self.contour(ship)

    def out_field(self, x, y):
        return not ((0 <= x < self.size) and (0 <= y < self.size))

    def shoot(self, dot):
        if self.out_field(dot.x, dot.y):
            raise BoardOutException()
        if dot in self.busy:
            raise RepeatBordException()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.wound()
                self.board[dot.x][dot.y] = 'X'
                if not ship.life:
                    self.count += 1
                    self.contour(ship, True)
                    print("Корабль потоплен")
                    return False
                else:
                    print("Корабль ранен, но все еще на плаву. Стредяй еще")
                    return True

        self.board[dot.x][dot.y] = 'T'
        print('Мимо!')
        return False

    def begin(self):
        self.busy = []



