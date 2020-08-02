print("")
print("MY PYTHON SCRIPT")
print("less worries")


import sys
print("sys working")
sys.path.insert(1, '../code')
print("path updated")
import code as calc
print("code imported")
import unittest
print("unittest imported")

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

print("class defined")

if (__name__ == "__main__"):
    unittest.main()
    print("I am here")

print("hmmmmmm")