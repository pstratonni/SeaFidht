from Dot import Dot
from MyException import *
from Ship import Ship


class Board:
    def __init__(self, hid):
        self.board = [['-' for j in range(6)] for i in range(6)]
        self.hid = hid

        self.count = 0
        self.busy = []
        self.ships = []

    def render(self):
        print('  |', end='\t')
        for i in range(6):
            print(f'{i + 1} |', end='\t')
        print()
        for i in range(6):
            print(f'{i + 1} |', end='\t')
            for j in range(6):
                print(f'{self.board[i][j]} |', end='\t')
            print()

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
                raise ShipOutException()
        for dot in ship.dots:
            self.board[dot.x][dot.y] = 'S'
            self.busy.append(dot)
        self.ships.append(ship)
        self.contour(ship)

    def out_field(self, x, y):
        return not ((0 <= x < 6) and (0 <= y < 6))

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



