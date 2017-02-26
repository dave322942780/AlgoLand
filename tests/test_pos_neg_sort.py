import unittest

from pos_neg_sort import solution


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], solution([]))

    def test_singles(self):
        neg_num = -3
        pos_num = 1
        self.assertEqual([neg_num], solution([neg_num]))
        self.assertEqual([pos_num], solution([pos_num]))

    def test_general(self):
        lst = [-1, 6, 3, -4, -6, 5, -6]
        actual_res = [-1, -4, -6, -6, 6, 3, 5]
        self.assertEqual(actual_res, solution(lst))
        self.assertEqual(actual_res, lst)
