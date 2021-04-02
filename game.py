import pyxel
from snake import Snake
from point import Point
from fruit import Fruit
from direction import Direction


class Game:

    width = 80
    height = 80
    title = "SNAKE GAME"

    def __init__(self):
        min = Point(0, 10)
        max = Point(self.width-1, self.height-1)
        pyxel.init(self.width, self.height, caption=self.title, fps=18)
        pyxel.load("my_resource.pyxres")
        self.snake = Snake(self.width / 2, self.height / 2)
        self.fruits = [
            Fruit(min, max, 8),
            Fruit(min, max, 9),
            Fruit(min, max, 10)
        ]
        self.direction = Direction()
        self._reset()
        pyxel.run(self.update, self.draw)

    def _reset(self):
        self.direction.up()
        self.points = 0
        self.snake.reset()
        for fruit in self.fruits:
            fruit.reset()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if not self.snake.alive and pyxel.btnp(pyxel.KEY_R):
            self._reset()

        for fruit in self.fruits:
            self._checkFruitEaten(fruit)

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
        if self.snake.alive:
            for fruit in self.fruits:
                self._drawFruit(fruit)

    def _drawSnake(self):
        if self.snake.alive:
            snake_colors = [6, 12, 5, 1]
            idx_color = 1
            for part in self.snake.body:
                pyxel.pset(part.x, part.y, snake_colors[idx_color-1])
                idx_color = min((idx_color+1), len(snake_colors))

    def _drawGameOver(self):
        if not self.snake.alive:
            for part in self.snake.body:
                pyxel.pset(part.x, part.y, 8)
            text = "PRESS R TO RESTART"
            pyxel.text(5, 40, text, 1)

    def _drawFruit(self, fruit):
        if fruit.eaten:
            fruit.reset()
        pyxel.pset(fruit.x, fruit.y, fruit.color)

    def _drawHeader(self):
        pyxel.rect(0, 0, 80, 9, 2)
        pyxel.text(12, 2, self.title, 8)
        points = str(self.points)
        x = 79 - (len(points) * 5) + len(points)
        pyxel.text(x, 2, points, 10)
        pyxel.blt(2, 0, 0, 0, 0, 8, 8, 0)

    def _checkFruitEaten(self, fruit):
        if self.snake.head == fruit.position:
            fruit.eaten = True
            self.points += 1
            self.snake.grow()
            pyxel.playm(0, loop=False)

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
        if head.x >= self.width or head.x < 0 or head.y >= self.height or head.y < 9:
            self.snake.alive = False


Game()
