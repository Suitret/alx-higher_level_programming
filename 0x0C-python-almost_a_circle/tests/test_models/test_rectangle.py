import unittest
import sys
from io import StringIO
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
        self.assertEqual(rect2.id, 2)

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

    def test_area(self):
        """Test area calculation
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

        rect.width = 8
        rect.height = 12
        self.assertEqual(rect.area(), 96)

    def test_display(self):
        """Test display method
        """
        rect = Rectangle(3, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        expected_output = "###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        rect2 = Rectangle(4, 3, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect2.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        rect3 = Rectangle(1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect3.display()
        sys.stdout = sys.__stdout__
        expected_output = "#\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method
        """
        rect = Rectangle(5, 10, 2, 1, 4)
        self.assertEqual(str(rect), "[Rectangle] (4) 2/1 - 5/10")

        rect2 = Rectangle(3, 2, 0, 0)
        self.assertEqual(str(rect2), "[Rectangle] (8) 0/0 - 3/2")

    def test_update_no_keyword_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_partial_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_single_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
