from fake import Fake
import unittest

class TestFakeClass(unittest.TestCase):

    def setUp(self):
        self.d = Fake()  # Initialize the Fake object

    def test_1(self):
        self.assertEqual(self.d.tri_recursion(4), 10)

if __name__ == '__main__':
    unittest.main()