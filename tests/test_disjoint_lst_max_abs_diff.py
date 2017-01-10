# https://careercup.com/question?id=19286747
import unittest

from disjoint_lst_max_abs_diff import solution


class MyTestCase(unittest.TestCase):
    def test_disjoint_lst_max_abs_diff(self):
        lst = [2, -1, -2, 1, -4, 2, 8]
        self.assertEqual(solution(lst), [[-1, -2, 1, -4], [2, 8], 16])

    def test_disjoint_lst_max_abs_diff_2(self):
        lst = [2, -1, -2, 1, -4, 2, 8, -1]
        self.assertEqual(solution(lst), [[-1, -2, 1, -4], [2, 8], 16])

    def test_disjoint_lst_max_abs_diff_3(self):
        lst = [-1, -2, 1, -4, 2, 8, -1]
        self.assertEqual(solution(lst), [[-1, -2, 1, -4], [2, 8], 16])

    def test_disjoint_lst_max_abs_diff_4(self):
        lst = [-1, -2, 1, -4, 2, 8]
        self.assertEqual(solution(lst), [[-1, -2, 1, -4], [2, 8], 16])


