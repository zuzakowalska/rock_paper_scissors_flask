import random


class Game:
    def __init__(self, moves):
        self.moves = moves

    def setup(self, move):
        self.u = move
        if self.u in list(self.moves.values()):
            self.u = list(self.moves.keys())[
                list(self.moves.values()).index(self.u)]
        self.cp = random.choice(list(self.moves.keys()))
        self.cp_name = self.moves[self.cp]
        return self

    def round_check(self):
        self.round_score = self.u - self.cp
        if self.round_score in [-1, 2]:
            return 1
        elif self.round_score in [-2, 1]:
            return -1
        elif self.round_score == 0:
            return 0
