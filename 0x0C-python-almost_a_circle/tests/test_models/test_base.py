import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class
    """

    def test_init_with_id(self):
        """Test constructor with id argument
        """
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_without_id(self):
        """Test constructor without id argument
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)


if __name__ == '__main__':
    unittest.main()
