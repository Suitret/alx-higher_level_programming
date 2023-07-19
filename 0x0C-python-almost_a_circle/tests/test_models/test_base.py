import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        rect_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        square_dict = {"id": 2, "size": 3, "x": 4, "y": 5}
        list_dict = [rect_dict, square_dict]

        json_string = Base.to_json_string(list_dict)
        self.assertEqual(json_string, '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
                                      '{"id": 2, "size": 3, "x": 4, "y": 5}]')

    def test_save_to_file(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        square1 = Square(5)
        square2 = Square(6)

        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, '
                                      '{"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}]')

        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 3, "size": 5, "x": 0, "y": 0}, '
                                      '{"id": 4, "size": 6, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        json_string = None
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(list_objs, [])

        json_string = ""
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(list_objs, [])

        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, ' \
                      '{"id": 2, "size": 3, "x": 4, "y": 5}]'
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(len(list_objs), 2)
#        self.assertIsInstance(list_objs[0], Rectangle)
#        self.assertIsInstance(list_objs[1], Square)
        self.assertEqual(list_objs[0]['id'], 1)
        self.assertEqual(list_objs[0]['width'], 2)
        self.assertEqual(list_objs[0]['height'], 3)
        self.assertEqual(list_objs[0]['x'], 4)
        self.assertEqual(list_objs[0]['y'], 5)
        self.assertEqual(list_objs[1]['id'], 2)
        self.assertEqual(list_objs[1]['size'], 3)
        self.assertEqual(list_objs[1]['x'], 4)
        self.assertEqual(list_objs[1]['y'], 5)

    def test_create(self):
        rect_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        square_dict = {"id": 2, "size": 3, "x": 4, "y": 5}

        rect1 = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect1, Rectangle)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 4)
        self.assertEqual(rect1.y, 5)

        square1 = Square.create(**square_dict)
        self.assertIsInstance(square1, Square)
        self.assertEqual(square1.id, 2)
        self.assertEqual(square1.size, 3)
        self.assertEqual(square1.x, 4)
        self.assertEqual(square1.y, 5)

    def test_load_from_file(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        square1 = Square(5)
        square2 = Square(6)

        rect_instances = [rect1, rect2]
        square_instances = [square1, square2]

        Rectangle.save_to_file(rect_instances)
        rect_loaded = Rectangle.load_from_file()
        self.assertEqual(len(rect_loaded), 2)
        self.assertIsInstance(rect_loaded[0], Rectangle)
        self.assertIsInstance(rect_loaded[1], Rectangle)
        self.assertEqual(rect_loaded[0].id, 1)
        self.assertEqual(rect_loaded[0].width, 1)
        self.assertEqual(rect_loaded[0].height, 2)
        self.assertEqual(rect_loaded[0].x, 0)
        self.assertEqual(rect_loaded[0].y, 0)
        self.assertEqual(rect_loaded[1].id, 2)
        self.assertEqual(rect_loaded[1].width, 3)
        self.assertEqual(rect_loaded[1].height, 4)
        self.assertEqual(rect_loaded[1].x, 0)
        self.assertEqual(rect_loaded[1].y, 0)

        Square.save_to_file(square_instances)
        square_loaded = Square.load_from_file()
        self.assertEqual(len(square_loaded), 2)
        self.assertIsInstance(square_loaded[0], Square)
        self.assertIsInstance(square_loaded[1], Square)
        self.assertEqual(square_loaded[0].id, 3)
        self.assertEqual(square_loaded[0].size, 5)
        self.assertEqual(square_loaded[0].x, 0)
        self.assertEqual(square_loaded[0].y, 0)
        self.assertEqual(square_loaded[1].id, 4)
        self.assertEqual(square_loaded[1].size, 6)
        self.assertEqual(square_loaded[1].x, 0)
        self.assertEqual(square_loaded[1].y, 0)


if __name__ == "__main__":
    unittest.main()
