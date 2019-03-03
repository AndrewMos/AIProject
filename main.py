from engine import Canvas
import random, time


canvas = Canvas(20, 20, '*')
while True:
    canvas.point(random.randint(1, 20), random.randint(1, 20), '@')
    canvas.draw()
    time.sleep(3)
    canvas.clear()
