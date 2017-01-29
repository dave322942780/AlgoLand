import unittest

from longest_sequential_subset import solution


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual([4], solution([4]))

    def test_all(self):
        self.assertEqual([5, 6, 7], solution([6, 5, 1, 10, 7]))

    def test_general(self):
        self.assertEqual([4, 5, 6, 7], solution([6, 10, 4, 7, 9, 5]))
