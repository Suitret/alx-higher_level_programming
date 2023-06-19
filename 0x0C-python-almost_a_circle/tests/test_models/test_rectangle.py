import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
    """

    def test_constructor(self):
        """Test constructor with various arguments
        """
        rect1 = Rectangle(10, 20, 1, 2, 3)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 20)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.y, 2)
        self.assertEqual(rect1.id, 3)

        rect2 = Rectangle(5, 10)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 10)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)
        self.assertEqual(rect2.id, None)

    def test_setters(self):
        """Test setters for width, height, x, and y attributes
        """
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

        rect.height = 25
        self.assertEqual(rect.height, 25)

        rect.x = 3
        self.assertEqual(rect.x, 3)

        rect.y = 4
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
