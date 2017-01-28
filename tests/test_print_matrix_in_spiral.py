import unittest

from print_matrix_in_spiral import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        self.assertEqual([1], solution([[1]]))

    def test_even_row_odd_column(self):
        self.assertEqual([1, 2, 3, 6, 9, 7, 6, 5, 7, 4, 5, 8],
                         solution([
                             [1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9],
                             [5, 6, 7]
                         ]))

    def test_even_column_odd_row(self):
        self.assertEqual([1, 2, 3, 4, 9, 5, 4, 3, 2, 6, 7, 8],
                         solution([
                             [1, 2, 3, 4],
                             [6, 7, 8, 9],
                             [2, 3, 4, 5]
                         ]))

    def test_odd_both(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5],
                         solution([
                             [1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]
                         ]))

    def test_even_both(self):
        self.assertEqual([1, 2, 3, 4, 7, 6, 8, 7, 6, 5, 7, 4, 5, 6, 9, 8],
                         solution([
                             [1, 2, 3, 4],
                             [4, 5, 6, 7],
                             [7, 8, 9, 6],
                             [5, 6, 7, 8]
                         ]))
