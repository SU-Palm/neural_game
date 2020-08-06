import pygame
from obj.brain import Brain
BLACK = (0,   0,   0)
max_x_pos = 1000
max_y_pos = 0


class Dot:
    def __init__(self, width, height):
        self.brain = Brain(400)
        self.random = self.brain.randomize_dot(400)
        self.pos = [round(width/2), round(height/2)]  # Need to get display width and height
        self.vel = [0.0, 0.0]
        self.acc = [0.0, 0.0]
        self.fillcolor = BLACK

    def show_dot(self, surface=None):
        if not surface: surface = pygame.display.get_surface()
        pygame.draw.circle(surface, self.fillcolor,  ((round(self.pos[0])), (round(self.pos[1]))), 4)

    def move_dot(self):
        e = self.pos
        if self.brain.size > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        x = self.acc[0]
        y = self.acc[1]
        if self.vel[0] <= 5:
            self.vel[0] = self.vel[0] + x
        if self.vel[1] <= 5:
            self.vel[1] = self.vel[1] + y
        x = self.vel[0]
        y = self.vel[1]
        self.pos[0] = e[0] + x
        self.pos[1] = e[1] - y
