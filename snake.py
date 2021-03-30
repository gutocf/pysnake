import copy
from point import Point


class Snake:

    body = []
    alive = True
    last_tail = False
    initial_point = False

    def __init__(self, start_x, start_y):
        self.initial_point = Point(start_x, start_y)
        self.reset()

    def reset(self):
        self.body = [self.initial_point]
        self.alive = True

    @property
    def head(self):
        return self.body[0]

    def move(self, direction):
        self.last_tail = copy.copy(self.body[-1])
        head = self.move_head(direction)
        self.body.pop()
        self.body.insert(0, head)
        self.checkTouchItSelf()

    def move_head(self, direction):
        head = copy.copy(self.head)
        if(direction.get_up()):
            head.moveUp()
        if(direction.get_down()):
            head.moveDown()
        if(direction.get_left()):
            head.moveLeft()
        if(direction.get_right()):
            head.moveRight()
        return head

    def checkTouchItSelf(self):
        index = 1
        if len(self.body) > 3:
            for part in self.body:
                if self.body[index:].count(part) == 1:
                    self.alive = False
                    break
                index += 1

    def grow(self):
        self.body.append(self.last_tail)
