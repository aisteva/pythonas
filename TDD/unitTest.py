import unittest

# Here's our "unit".
def oddNumber(x):
    return x % 2 == 1


class TestOddNumer(unittest.TestCase):

    def testWithOdd(self):
        self.assertTrue(oddNumber(5))

    def testWithNotOdd(self):
        self.assertFalse(oddNumber(2))

    def testWithMath(self):
        number = 5 + 5
        self.assertFalse(oddNumber(number))

    def testWithEqualsOdd(self):
        self.assertEqual(oddNumber(2), oddNumber(4))

    def testWithNotEqualsOdd(self):
        self.assertEqual(oddNumber(5), oddNumber(7))

def main():
    unittest.main()

if __name__ == '__main__':
    main()