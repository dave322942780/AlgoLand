# https://careercup.com/question?id=19286747
import unittest

from longest_sequential_subset import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        self.assertTrue([5], solution([5]))

    def test_multi(self):
        self.assertTrue([5, 6, 7, 8], solution([5, 7, 8, 2, 1, 6]))
        self.assertTrue([5, 6, 7, 8], solution([5, 7, 8, 6]))
