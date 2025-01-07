from multiplication import multiply
import unittest

class TestMultiplyClass(unittest.TestCase):

    def setUp(self):
        self.d = multiply()  # Initialize the Multiply object

    def test_1(self):
        self.assertEqual(self.d.multiply(5, 5), 25)

    def test_2(self):
        self.assertEqual(self.d.multiply(5, 10), 50)

    def test_3(self):
        self.assertEqual(self.d.multiply(2, 1), 2)

    def test_4(self):
        self.assertEqual(self.d.multiply(3, 0.5), 1.5)

    def test_5(self):
        self.assertEqual(self.d.multiply(1000, 5), 5000)

    def test_6(self):
        self.assertEqual(self.d.multiply(990, 33), 1)

if __name__ == '__main__':
    unittest.main()