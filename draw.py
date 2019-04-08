import random, time
import sys, pygame
import numpy as np


def draw(map, steps):
    pygame.init()
    grid = pygame.image.load("media/grid.png")
    home = pygame.image.load("media/home.png")
    agent = pygame.image.load("media/agent.png")
    warehouse = pygame.image.load("media/warehouse.png")
    step = pygame.image.load("media/step.png")
    gridrect = agent.get_rect()
    homerect = home.get_rect()
    agentrect = agent.get_rect()
    warehouserect = warehouse.get_rect()
    steprect = step.get_rect()
    w, h = gridrect.width, gridrect.height

    size = width, height = len(map[0])*w, len(map)*h
    screen = pygame.display.set_mode(size)
    y = h/2
    for line in map:
        x = w/2
        for obj in line:
            if obj == ' ':
                gridrect.center = (x, y)
                screen.blit(grid, gridrect)
            if obj == '#':
                homerect.center = (x, y)
                screen.blit(home, homerect)
            if obj == 'o':
                agentrect.center = (x, y)
                screen.blit(agent, agentrect)
            if obj == 'x':
                warehouserect.center = (x, y)
                screen.blit(warehouse, warehouserect)

            x += w
        y += h


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for s in steps[1:-1]:
            steprect.center = (s[0]*w + w/2, s[1]*h+h/2)
            screen.blit(step, steprect)
            pygame.display.flip()
            time.sleep(0.4)
