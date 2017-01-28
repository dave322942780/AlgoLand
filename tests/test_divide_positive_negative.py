import unittest

from divide_negative_positive import solution


class MyTestCase(unittest.TestCase):
    def test_negatives(self):
        negative_lst = [-2, -4, -6, -7]
        solution(negative_lst)
        self.assertEqual(negative_lst, [-2, -4, -6, -7])

    def test_positives(self):
        positive_lst = [2, 4, 6, 7]
        solution(positive_lst)
        self.assertEqual(positive_lst, [2, 4, 6, 7])

    def test_negative_positive(self):
        lst = [-2, -3, -5, -10, 2, 4, 6, 7]
        solution(lst)
        self.assertEqual(lst, [-2, -3, -5, -10, 2, 4, 6, 7])

    def test_positive_negative(self):
        lst = [2, 4, 6, 7, -2, -3, -5, -10]
        solution(lst)
        self.assertEqual(lst, [-2, -3, -5, -10, 2, 4, 6, 7])

    def test_mixed(self):
        lst = [-3, 2, 4, -2, 6, 7, -5, -10]
        solution(lst)
        self.assertEqual(lst, [-3, -2, -5, -10, 2, 4, 6, 7])
