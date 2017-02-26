import unittest

from merge_intervals import solution


class MyTestCase(unittest.TestCase):
    def test_general(self):
        self.assertEqual(3, solution([[1, 4], [2, 3]]))
        self.assertEqual(3, solution([[4, 6], [1, 2]]))
        self.assertEqual(11, solution([[1, 4], [6, 8], [2, 4], [7, 9], [10, 15]]))
