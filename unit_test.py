import unittest
from main import multiply

class testMulti(unittest.TestCase):
    def testMulti1(self):
        self.assertEqual(multiply(3, 4), 12)
    def testMulti2(self):
        self.assertEqual(multiply(5, 6), 30)
    def testMulti3(self):
        self.assertEqual(multiply(7, 7), 49)

if __name__ == '__main__':
    unittest.main()

