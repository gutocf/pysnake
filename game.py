import pyxel
from random import randint

WIDTH = 80
HEIGHT = 80
COLOR_BG = 0
COLOR_BG_DEAD = 4
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


class Game:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="SNAKE GAME", fps=20)
        pyxel.load("my_resource.pyxres", True, False, False, False)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.snake_x = WIDTH / 2
        self.snake_y = HEIGHT / 2
        self.dir = randint(1,4)
        self.dead = False
        self.hasApple = False
        self.apple_x = 0
        self.apple_y = 0
        self.points = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.dead and pyxel.btnp(pyxel.KEY_R):
            self.reset()

        self.checkAppleEaten()
        self.changeDir()
        self.move()

    def checkAppleEaten(self):
        if self.snake_x == self.apple_x and self.snake_y == self.apple_y:
            self.hasApple = False
            self.points += 1

    def changeDir(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.dir = UP

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.dir = DOWN

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.dir = LEFT

        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.dir = RIGHT

    def move(self):
        if self.dir == UP:
            self.snake_y -= 1

        if self.dir == RIGHT:
            self.snake_x += 1

        if self.dir == DOWN:
            self.snake_y += 1

        if self.dir == LEFT:
            self.snake_x -= 1

        if self.snake_x == 80 or self.snake_x == 0 or self.snake_y == 80 or self.snake_y == 5:
            self.dead = True

    def draw(self):

        if self.dead == False:
            pyxel.cls(col=COLOR_BG)

        if self.dead == True:
            pyxel.cls(5)

        self.drawHeader()
        self.drawSnake()

    def drawSnake(self):
        if self.dead == False:
            pyxel.pset(self.snake_x, self.snake_y, 3)
            self.drawApple()

        if self.dead == True:
            pyxel.text(22, 40, "GAME OVER", 1)

    def drawApple(self):
        if self.hasApple == False:
            self.apple_x = randint(0, WIDTH - 1)
            self.apple_y = randint(20, HEIGHT)
            self.hasApple = True

        pyxel.pset(self.apple_x, self.apple_y, 8)

    def drawHeader(self):
        pyxel.text(12, 2, "SNAKE GAME", 8)
        points = str(self.points)
        x = 79 - (len(points) * 5) + len(points)
        pyxel.text(x, 2, points, 10)
        pyxel.blt(2, 0, 0, 0, 0, 8, 8, 0)


Game()
