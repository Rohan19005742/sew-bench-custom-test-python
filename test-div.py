from task1 import Divide
import unittest

class TestDivideClass(unittest.TestCase):

    def setUp(self):
        self.d = Divide()  # Initialize the Divide object

    def test_1(self):
        self.assertEqual(self.d.divide(5, 5), 1)

    def test_2(self):
        self.assertEqual(self.d.divide(5, 10), 0.5)

    def test_3(self):
        self.assertEqual(self.d.divide(2, 1), 2)

    def test_4(self):
        self.assertEqual(self.d.divide(3, 0.5), 6)

    def test_5(self):
        self.assertEqual(self.d.divide(1000, 5), 200)

    def test_6(self):
        self.assertEqual(self.d.divide(990, 33), 30)

if __name__ == '__main__':
    unittest.main()
