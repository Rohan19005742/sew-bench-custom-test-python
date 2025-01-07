from n import n
import unittest

class TestNClass(unittest.TestCase):

    def setUp(self):
        self.n = n()  # Initialize the n object

    def test_1(self):
        self.assertEqual(self.n.returnHello(), "Hello")

if __name__ == '__main__':
    unittest.main()