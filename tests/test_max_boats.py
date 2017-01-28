import unittest

from max_boats import solution


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, solution([4]))

    def test_two(self):
        self.assertEqual(2, solution([4, 146]))
        self.assertEqual(1, solution([5, 146]))

    def test_multi(self):
        self.assertEqual(3, solution([80, 80, 80]))
        self.assertEqual(2, solution([80, 70, 80]))
        self.assertEqual(2, solution([10, 10, 10]))
