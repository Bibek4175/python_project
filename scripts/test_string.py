import unittest

from package.calculate_string import calculate_string

class TestStringLength(unittest.TestCase):
    def test_calculate_string(self):

        self.assertEqual(calculate_string("hello,world"),11)
        self.assertEqual(calculate_string(""),0)
        self.assertEqual(calculate_string(" "),1)


if __name__ =="__main__":
    unittest.main()
