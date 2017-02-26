import unittest

from sort_with_stacks import solution


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], solution([]))

    def test_single(self):
        self.assertEqual([1], solution([1]))

    def test_general(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], solution([5, 3, 2, 7, 9, 1, 4, 8, 6]))
        self.assertEqual([1, 2, 3], solution([3, 2, 1]))
