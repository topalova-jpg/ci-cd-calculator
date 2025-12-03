# test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(subtract(5, 10), -5)

if __name__ == '__main__':
    unittest.main()