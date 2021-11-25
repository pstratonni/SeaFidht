class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and other.y == self.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'
