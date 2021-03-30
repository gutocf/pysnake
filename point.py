class Point:

    __x = 0
    __y = 0

    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

    def moveLeft(self):
        self.x -= 1

    def moveRight(self):
        self.x += 1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"
