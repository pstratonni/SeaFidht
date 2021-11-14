class Dot:
    def __init__(self, dot):
        self.dot = dot

    def __eq__(self, other):
        return self.dot[0] == other.dot[0] and other.dot[1] == self.dot[1]
