import random, time
import sys, pygame
import numpy as np

pygame.init()
size = width, height = 400, 400


class Home:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

class Map:
    def __init__(self, width=1, height=1):
        self.grid = np.zeros(width*height, dtype=np.int32).reshape((width, height))
        self.homes = []
        # print(self.grid)
    def addhome(self, home):
        self.homes.append(home)
        self.grid[home.x][home.y] = 1


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
grid = pygame.image.load("media/grid.png")
home = pygame.image.load("media/home.png")
agent = pygame.image.load("media/agent.png")
gridrect = agent.get_rect()
homerect = home.get_rect()
agentrect = agent.get_rect()
w, h = gridrect.width, gridrect.height


def draw(m):
    for i in range(0, len(m.grid)):
        for j in range(0, len(m.grid[0])):
            if (m.grid[i][j] == 0):
                gridrect.center = (i*width/w + w/2, j*height/h + h/2)
                screen.blit(grid, gridrect)
            if (m.grid[i][j] == 1):
                homerect.center = (i*width/w + w/2, j*height/h + h/2)
                screen.blit(home, homerect)


robot = Agent(5, 5)
m = Map(20, 20)
coordinates = [[2,2], [2,4], [2,6], [6,2], [6,5], [6, 8], [6, 11], [10, 2], [10, 6]]
for line in coordinates:
    hm = Home(line[0], line[1], "Andrew")
    m.addhome(hm)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                robot.goleft()
            if event.key == pygame.K_RIGHT:
                robot.goright()
            if event.key == pygame.K_UP:
                robot.goup()
            if event.key == pygame.K_DOWN:
                robot.godown()
    # inp = input().split()
    inp = [0]
    for dir in inp:
        draw(m)
        # screen.fill([0, 0, 0, 0])
        # robot.go(random.randint(0, 3))
        # robot.go(int(dir))
        agentrect.center = (robot.x * w + w/2, robot.y * h + h/2)
        screen.blit(agent, agentrect)
        pygame.display.flip()
        # time.sleep(0.1)
