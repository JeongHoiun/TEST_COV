import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        self.calculator.add(10)
        self.assertEqual(self.calculator.get_result(), 10)
    
    def test_sub(self):
        self.calculator.sub(5)
        self.assertEqual(self.calculator.get_result(), -5)
    
    def test_mul(self):
        self.calculator.mul(3)
        self.assertEqual(self.calculator.get_result(), 0)
    
    def test_div(self):
        self.calculator.div(2)
        self.assertEqual(self.calculator.get_result(), 0)
    
    def test_reset(self):
        self.calculator.reset()
        self.assertEqual(self.calculator.get_result(), 0)
    
    def test_set_result(self):
        self.calculator.set_result(100)
        self.assertEqual(self.calculator.get_result(), 100)
    
    def tearDown(self):
        del self.calculator

if __name__ == '__main__': # pragma: no cover
    unittest.main()

# Path: calculator.test.py
# $ python calculator.test.py
# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.000s
#
# OK
# $ python calculator.test.py -v