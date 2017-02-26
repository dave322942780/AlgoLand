import unittest

from max_range_less_than import solution


class MyTestCase(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(solution([1]))

    def test_general(self):
        self.assertEqual((0, 6), solution([1, 4, 4, 5, 1, 5, 2]))
        self.assertEqual((1, 5), solution([6, 4, 4, 5, 1, 5, 2]))
