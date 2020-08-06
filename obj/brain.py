import numpy as np
import random


class Brain:
    def __init__(self, size):
        self.step = 0
        self.size = size
        self.directions = np.zeros((400, 2))

    def randomize_dot(self, size):
        for x in range(0, size):
            determ = random.random()
            if determ >= .499:
                randomang1 = random.random()
            else:
                randomang1 = random.random() - 1
            if randomang1 > 0:
                randomang2 = 1 - randomang1
            else:
                randomang2 = 1 + randomang1
            self.directions[x] = np.array([randomang1, randomang2])
