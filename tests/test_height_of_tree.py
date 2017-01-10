import unittest

from height_of_tree import solution


class MyTestCase(unittest.TestCase):
    def test_height_of_Tree(self):
        self.assertEqual(2, solution([3, 3, -1, 2]))
