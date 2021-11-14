from Dot import Dot


class Ship:
    def __init__(self, bow, length, orientation):
        self.bow = Dot(bow)
        self.length = length
        self.orientation = orientation
        self.life = length

    def wound(self):
        self.life -= 1

    @property
    def dots(self):
        if self.orientation == 'V':
            return [Dot(tuple(self.bow.dot[0], self.bow.dot[1] + j)) for j in range(self.length)]
        else:
            return [Dot(tuple(self.bow.dot[0] + i, self.bow.dot[1])) for i in range(self.length)]

