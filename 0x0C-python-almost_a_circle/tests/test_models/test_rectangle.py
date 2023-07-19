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
        self.assertEqual(str(rect2), "[Rectangle] (17) 0/0 - 3/2")

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

    def test_to_json_string_empty_list(self):
        result = Rectangle.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        result = Rectangle.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        result = Rectangle.to_json_string(list_rectangles_input)
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r") as file:
            result = file.read()
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
        self.assertEqual(result, expected)

    def test_from_json_string_empty_string(self):
        result = Rectangle.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        result = Rectangle.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string(self):
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
        result = Rectangle.from_json_string(json_string)
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        expected = [r1, r2]
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertIsInstance(result[i], Rectangle)
            self.assertEqual(result[i].to_dictionary(), expected[i].to_dictionary())

    def test_create(self):
        dictionary = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        result = Rectangle.create(**dictionary)
        expected = Rectangle(10, 7, 2, 8, 1)
        self.assertIsInstance(result, Rectangle)
        self.assertEqual(result.to_dictionary(), expected.to_dictionary())

    def test_load_from_file_empty_file(self):
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_file_not_found(self):
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), len(list_rectangles_input))
        for i in range(len(result)):
            self.assertIsInstance(result[i], Rectangle)
            self.assertEqual(result[i].to_dictionary(), list_rectangles_input[i].to_dictionary())


if __name__ == '__main__':
    unittest.main()
