from random import randint
from point import Point


class Fruit:

    def __init__(self, min, max, color):
        self.position = Point(0, 0)
        self.eaten = False
        self.min = min
        self.max = max
        self.color = color
        self.reset()

    def reset(self):
        self.position.x = randint(self.min.x, self.max.x)
        self.position.y = randint(self.min.y, self.max.y)
        self.eaten = False

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y
