import numpy as np
from obj.dot import Dot
d_width = 1000
d_height = 1000
c = np.zeros(400)
thing = np.array(c, dtype=Dot)
BLACK = (0,   0,   0)


class Population:
    def __init__(self, sze):
        for x in range(0, sze):
            dot = Dot(d_width, d_height)
            thing[x] = dot
        self.dots = thing
        self.gen = 1
        self.fitnessSum = 0
        self.minstep = 1000
        self.size = sze
        self.bestDot = self.dots[0]
        self.totalDif = 5000000

    def show_dots(self):
        for i in range(0, self.size):
            joe = self.dots[i]
            joe.show_dot()

    def move_dots(self):
        for i in range(0, self.size):
            joe = self.dots[i]
            if joe.pos[0] > 1000 or joe.pos[0] < 0 or joe.pos[1] < 0:
                print("Deleted")
                # del joe
            else:
                joe.move_dot()

    def fitness_calc(self, target):
        print("Print Size of the Array of ")
        for i in range(0, self.size):
            dif_x = target[0] - self.dots[i].pos[0]
            if dif_x < 0:
                dif_x = dif_x * -1
            dif_y = target[1] - self.dots[i].pos[1]
            if dif_y < 0:
                dif_y = dif_y * -1
            totaldif = dif_x + dif_y
            if self.totalDif > totaldif:
                self.totalDif = totaldif
                self.bestDot = self.dots[i]
        print("Printing Best Dot: ", self.bestDot.pos)
        print("Printing Best Diff", self.totalDif)
