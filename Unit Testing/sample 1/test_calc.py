import calc
import unittest

class TestCalc(unittest.TestCase):

    result = calc.Calculator()

    def test_add(self):
        self.assertEqual(self.result.add(4, 6), 10)

    def test_subtract(self):
        self.assertEqual(self.result.subtract(8, 4), 4)

    def test_multiply(self):
        self.assertEqual(self.result.multiply(5, 2), 10)

    def test_division(self):
        self.assertEqual(self.result.division(9, 3), 3)

    def test_square_root(self):
        self.assertEqual(self.result.square_root(16), 4)

    def test_power(self):
        self.assertEqual(self.result.power(6, 4), 1296)

if __name__ == "__main__":
    unittest.main()
