import unittest
from operations import add, subtract, multiply, divide

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(6, 0)

if __name__ == '__main__':
    unittest.main()
