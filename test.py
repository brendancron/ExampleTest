import sys
sys.path.insert(1, '../code')
import code as calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(3,4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = calc.subtract(9,7)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = calc.multiply(4,5)
        self.assertEqual(result, 20)

    def test_div(self):
        result = calc.divide(30,5)
        self.assertEqual(result, 6)

if (__name__ == "__main__"):
    unittest.main()
    print("I am here")

print("hmmmmmm")