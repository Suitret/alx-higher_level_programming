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

    def test_invalid_setters(self):
        """Test invalid values in setters
        """
        rect = Rectangle(5, 10)

        with self.assertRaises(TypeError):
            rect.width = "not_an_integer"
        with self.assertRaises(TypeError):
            rect.height = "not_an_integer"
        with self.assertRaises(TypeError):
            rect.x = "not_an_integer"
        with self.assertRaises(TypeError):
            rect.y = "not_an_integer"

        with self.assertRaises(ValueError):
            rect.width = 0
        with self.assertRaises(ValueError):
            rect.height = -5
        with self.assertRaises(ValueError):
            rect.x = -2
        with self.assertRaises(ValueError):
            rect.y = -3


if __name__ == '__main__':
    unittest.main()
