from random import randint
from point import Point


class Apple:

    position = Point(0, 0)
    min = Point(0, 0)
    max = Point(0, 0)
    eaten = False

    def __init__(self, min, max):
        self.min = min
        self.max = max
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
