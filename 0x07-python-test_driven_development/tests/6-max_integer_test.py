import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_strings_instead_of_ints(self):
        self.assertEqual(max_integer(["K", "r", "a", "f", "t"]), "t")

    def test_strings_and_int(self):
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_basic_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_basic_two_els(self):
        self.assertEqual(max_integer([1,2]), 2)

    def test_basic_all_negatives(self):
        self.assertEqual(max_integer([-2, -1]), -1)

    def test_basic_negative_zero_zero(self):
        self.assertEqual(max_integer([-1, 0]), 0)

    def test_basic_(self):
        self.assertEqual(max_integer([6, 1, 2, 3]), 6)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-5, -3, -1, -4, -2]), -1)


if __name__ == '__main__':
    unittest.main()
