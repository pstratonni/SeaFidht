from Dot import Dot


class Ship:
    def __init__(self, bow, length, orientation):
        self.bow = bow
        self.length = length
        self.orientation = orientation
        self.life = length

    def wound(self):
        self.life -= 1

    @property
    def dots(self):

        if self.orientation == 'H':
            return [Dot(self.bow.x, self.bow.y + j) for j in range(self.length)]
        else:
            return [Dot(self.bow.x + i, self.bow.y) for i in range(self.length)]
