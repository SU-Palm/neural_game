import pygame
from obj.dot import Dot
from obj.population import Population
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
pygame.init()
d_width = 1000
d_height = 1000
DISPLAYSURF = pygame.display.set_mode((d_width, d_height))
DISPLAYSURF.fill(WHITE)
FPS = 40
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Machine Learning')
running = True
population = Population(300)
dot = Dot(d_width, d_height)
target = [500, 30]
while running:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, BLACK, (500, 30), 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("QUITTING NOW...")
                pygame.time.delay(1000)
                running = False
    population.move_dots()
    population.show_dots()
    population.fitness_calc(target)
    pygame.display.update()
    fpsClock.tick(FPS)
