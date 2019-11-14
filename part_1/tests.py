import unittest
from part_1.karatsuba import karatsuba


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(karatsuba(10,10), 100)

    def test_video(self):
        self.assertEqual(karatsuba(1234,5678), 7006652)

    def test_uneven_power(self):
        self.assertEqual(karatsuba(123,45), 5535)
        self.assertEqual(karatsuba(45,123), 5535)
        self.assertEqual(karatsuba(123,145), 17835)


if __name__ == '__main__':
    unittest.main()
