import time
import sys
import random

class Canvas:
    def draw(self):
        for line in self.grid:
            for element in line:
                sys.stdout.write(str(element) + " ")
                # sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.flush()

    def point(self, x, y):
        self.grid[y-1][x-1] = '@'

    def clear(self):
        for j in range(0, self.height):
            for i in range(0, self.width):
                self.grid[j][i] = '_'

    def redraw(self):
        sys.stdout.write("\033[F"*(self.height))
        # sys.stdout.flush()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        grid = []

        for j in range(0, height):
            temp = []
            for i in range(0, width):
                temp.append('*')
            grid.append(temp)
        self.grid = grid





canvas = Canvas(20, 20)
while True:
    canvas.point(random.randint(1, 20), random.randint(1, 20))
    canvas.draw()
    time.sleep(3)
    canvas.clear()
    canvas.redraw()
