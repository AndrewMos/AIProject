from engine import Canvas
import random, time

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acc = random.randint(1, 5) * 0.05
        self.speed = 0
    def move(self):
        self.speed += self.acc
        self.y += self.speed
        # print(self.speed)
    def check(self, height):
        if (self.y >= height):
            self.speed = -self.speed
            self.y = height


canvas = Canvas(20, 20)
balls = []
for i in range(canvas.width):
    ball = Ball(i, random.randint(0, 10))
    balls.append(ball)
while True:
    for ball in balls:
        canvas.point(ball.x, ball.y)
        ball.move()
        ball.check(canvas.height)


    canvas.draw()
    canvas.clear()
    time.sleep(0.1)

    # ball.x += random.randint(-1, 1)
    # ball.y += random.randint(-1, 1)
