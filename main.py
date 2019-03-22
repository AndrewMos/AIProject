from engine import Canvas
import random, time
import sys, pygame
pygame.init()

size = width, height = 400, 400


class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def go(self, dir):
        if (dir == 0):
            self.y += -1
        if (dir == 1):
            self.x += 1
        if (dir == 2):
            self.y += 1
        if (dir == 3):
            self.x += -1
    def goup(self):
        self.y += -1
    def goright(self):
        self.x += 1
    def godown(self):
        self.y += 1
    def goleft(self):
        self.x += -1

screen = pygame.display.set_mode(size)
grid = pygame.image.load("grid.png")
home = pygame.image.load("home.png")
agent = pygame.image.load("agent.png")
gridrect = agent.get_rect()
homerect = home.get_rect()
agentrect = agent.get_rect()
w, h = gridrect.width, gridrect.height

def background():
    for i in range(int(width / w)):
        for j in range(int(height / h)):
            gridrect.center = (i*width/w + w/2, j*height/h + h/2)
            screen.blit(grid, gridrect)


robot = Agent(5, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    inp = input().split()
    for dir in inp:
        background()
        robot.go(int(dir))
        agentrect.center = (robot.x * w + w/2, robot.y * h + h/2)
        screen.blit(agent, agentrect)
        pygame.display.flip()
        time.sleep(0.1)
