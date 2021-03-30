import unittest
from point import Point


class TestPoint(unittest.TestCase):

    def test_equals(self):
        p1 = Point()
        p2 = Point(0, 0)
        self.assertEqual(p1 == p2, True)
        p1 = Point()
        p2 = Point(0, 1)
        self.assertEqual(p1 == p2, False)
        p1 = Point()
        p2 = Point(1, 0)
        self.assertEqual(p1 == p2, False)
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertEqual(p1 == p2, True)

    def test_move_up(self):
        p1 = Point(10, 10)
        p1.moveUp()
        self.assertEquals(p1 == Point(10, 9), True)

    def test_move_down(self):
        p1 = Point(10, 10)
        p1.moveDown()
        print(p1)
        self.assertEquals(p1 == Point(10, 11), True)

    def test_move_right(self):
        p1 = Point(10, 10)
        p1.moveRight()
        self.assertEquals(p1 == Point(11, 10), True)

    def test_move_left(self):
        p1 = Point(10, 10)
        p1.moveLeft()
        self.assertEquals(p1 == Point(9, 10), True)


if __name__ == '__main__':
    unittest.main()
