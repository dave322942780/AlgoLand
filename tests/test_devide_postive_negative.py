import unittest
from divide_positive_negative import solution


class DividePositiveNegativeTestCase(unittest.TestCase):
    def test_negatives(self):
        negative_lst = [-2, -4, -6, -7]
        solution(negative_lst)
        self.assertEqual(negative_lst, [-2, -4, -6, -7])

    def test_positives(self):
        positive_lst = [2, 4, 6, 7]
        solution(positive_lst)
        self.assertEqual(positive_lst, [2, 4, 6, 7])

    def test_positive_negative(self):
        lst = [2, 4, 6, 7]
        solution(lst)
        self.assertEqual(lst, [2, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
