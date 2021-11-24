from Dot import Dot
from Player import Player
from random import randint
class All (Player):
    targets = []
    def add_targets (self):
        for i in range(6):
            for j in range(6):
                self.targets.append(Dot(i,j))

    def ask(self):
        idx=randint(0, len(self.targets)-1)
        dot=self.targets[idx]
        print(f'Ход компьютера({dot.x, dot.y})')
        self.targets.pop(idx)
        return dot



