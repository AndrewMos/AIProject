import time
import sys
import random

class Canvas:
    def draw(self, redrw=1):
        for line in self.grid:
            for element in line:
                sys.stdout.write(str(element) + " ")
                # sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.flush()
        if (redrw==1):
            self.redraw()

    # def floatpoint(self, x, y, char='@'):
    #     x = round(x)
    #     y = round(y)
    #     if (x >= 0 and x < self.width):
    #         if(y >= 0 and y < self.height):
    #             self.grid[y][x] = char

    def point(self, x, y, char='@'):
        x = round(x)
        y = round(y)
        if (x >= 0 and x < self.width):
            if(y >= 0 and y < self.height):
                self.grid[y][x] = char

    def clear(self):
        for j in range(0, self.height):
            for i in range(0, self.width):
                self.grid[j][i] = self.back

    def redraw(self):
        sys.stdout.write("\033[F"*(self.height))
        # sys.stdout.flush()

    def __init__(self, width, height, back='*'):
        self.width = width
        self.height = height
        self.back = back
        grid = []

        for j in range(0, height):
            temp = []
            for i in range(0, width):
                temp.append(back)
            grid.append(temp)
        self.grid = grid
