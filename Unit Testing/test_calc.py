import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(1, -1), 2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, -2), -2)
        self.assertEqual(calc.multiply(-1, -3), 3)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(12, -2), -6)
        self.assertEqual(calc.divide(-2, -2), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        ## test `exception` using `context manager`
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# python -m unittest test_calc
if __name__ == '__main__':
    unittest.main()
