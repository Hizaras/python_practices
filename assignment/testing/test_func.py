import unittest
from . import arithmetic

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_add(self):
        self.assertEqual(11, arithmetic.add(5, 6))

if __name__ == '__main__':
    unittest.main()
