import unittest

from h_index import solution


class MyTestCase(unittest.TestCase):
    def test_h_index(self):
        self.assertEqual(2, solution([1,2,3,4]))
        self.assertEqual(3, solution([900, 2, 901, 3, 1000]))
