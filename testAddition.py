from addition import Addition
import unittest

class TestAdditionClass(unittest.TestCase):

    def setUp(self):
        self.d = Addition()  # Initialize the Addition object

    def test_1(self):
        self.assertEqual(self.d.addition(5, 5), 10)

    def test_2(self):
        self.assertEqual(self.d.addition(5, 10), 15)

    def test_3(self):
        self.assertEqual(self.d.addition(2, 1), 3)

    def test_4(self):
        self.assertEqual(self.d.addition(3, 0.5), 3.5)

    def test_5(self):
        self.assertEqual(self.d.addition(1000, 5), 1005)

    def test_6(self):
        self.assertEqual(self.d.addition(99, 33), 132)

if __name__ == '__main__':
    unittest.main()