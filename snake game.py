import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = radndrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrtange(0, RES, SIZE)
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while TRUE:
    sc.fill(py.ganne.Color("black"))
    [(pygame.draw.rect(sc, pygame.Color("green"), (i, j, SIZE, SIZE))) for i, j, in snake]
    pygame.draw.rect(sc.pygame.Color('red'), (*apple, SIZE, SIZE))
    


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        
    
