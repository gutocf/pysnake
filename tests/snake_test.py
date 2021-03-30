import unittest
from point import Point
from snake import Snake


class TestSnake(unittest.TestCase):

    def test_create(self):
        p = Point(0, 0)
        snake = Snake(0, 0)
        self.assertTrue(p == snake.head)
        snake = Snake(0, 1)
        self.assertFalse(p == snake.head)
        snake = Snake(1, 0)
        self.assertFalse(p == snake.head)

if __name__ == '__main__':
    unittest.main()
