
import unittest
from direction import Direction

class TestDirection(unittest.TestCase):

    def test_up(self):
        dir = Direction()
        self.assertFalse(dir.get_up())
        dir.up()
        self.assertTrue(dir.get_up())

    def test_right(self):
        dir=Direction()
        self.assertFalse(dir.get_right())
        dir.right()
        self.assertTrue(dir.get_right())

    def test_down(self):
        dir=Direction()
        self.assertFalse(dir.get_down())
        dir.down()
        self.assertTrue(dir.get_down())

    def test_left(self):
        dir=Direction()
        self.assertFalse(dir.get_left())
        dir.left()
        self.assertTrue(dir.get_left())

if __name__ == '__main__':
    unittest.main()
