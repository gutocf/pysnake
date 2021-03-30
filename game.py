import pyxel
from snake import Snake
from point import Point
from apple import Apple
from direction import Direction

class Game:

    width = 80
    height = 80
    title = "SNAKE GAME"

    def __init__(self):
        pyxel.init(self.width, self.height, caption=self.title, fps=18)
        pyxel.load("my_resource.pyxres", True, False, False, False)
        self.snake = Snake(self.width / 2, self.height / 2)
        self.apple = Apple(Point(0, 20), Point(self.width, self.height))
        self.direction = Direction()
        self._reset()
        pyxel.run(self.update, self.draw)

    def _reset(self):
        self.direction.up()
        self.points = 0
        self.snake.reset()
        self.apple.reset()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if not self.snake.alive and pyxel.btnp(pyxel.KEY_R):
            self._reset()

        self._checkAppleEaten()
        self._changeDirection()
        self._moveSnake()

    def draw(self):
        if self.snake.alive:
            pyxel.cls(0)

        if not self.snake.alive:
            pyxel.cls(5)

        self._drawHeader()
        self._drawSnake()
        self._drawGameOver()

    def _drawSnake(self):
        if self.snake.alive:
            snake_colors = [6, 12, 5, 1]
            idx_color = 1
            for part in self.snake.body:
                pyxel.pset(part.x, part.y, snake_colors[idx_color-1])
                idx_color = min((idx_color+1), len(snake_colors))
            self._drawApple()

    def _drawGameOver(self):
        if not self.snake.alive:
            for part in self.snake.body:
                pyxel.pset(part.x, part.y, 8)
            text = "PRESS R TO RESTART"
            pyxel.text(5, 40, text, 1)

    def _drawApple(self):
        if self.apple.eaten:
            self.apple.reset()

        pyxel.pset(self.apple.x, self.apple.y, 8)

    def _drawHeader(self):
        pyxel.text(12, 2, self.title, 8)
        points = str(self.points)
        x = 79 - (len(points) * 5) + len(points)
        pyxel.text(x, 2, points, 10)
        pyxel.blt(2, 0, 0, 0, 0, 8, 8, 0)

    def _checkAppleEaten(self):
        if self.snake.head == self.apple.position:
            self.apple.eaten = True
            self.points += 1
            self.snake.grow()

    def _changeDirection(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction.up()

        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction.right()

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction.down()

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction.left()

    def _moveSnake(self):
        if(self.snake.alive):
            self.snake.move(self.direction)
            self._checkSnakeHitWalls()

    def _checkSnakeHitWalls(self):
        head = self.snake.head
        if head.x >= self.width or head.x <= 0 or head.y >= self.height or head.y <= 5:
            self.snake.alive = False


Game()
