import unittest

from find_duplicates import solution


class MyTestCase(unittest.TestCase):
    def test_find_duplicates(self):
        self.assertEqual({0, 1, 3}, set(solution([1, 1, 5, 3, 4, 0, 3, 0])))
