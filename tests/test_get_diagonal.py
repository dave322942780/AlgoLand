# https://careercup.com/question?id=19286747
import unittest

from get_diagional import solution


class GetDiagonalTestCase(unittest.TestCase):
    def test_get_diagonal_single(self):
        self.assertEqual(solution([[4]]), [[4]])

    def test_get_diagonal1(self):
        self.assertEqual(
                solution(
                        # matrix
                        [[1, 2],
                         [3, 4]]),
                # output
                [[1],
                 [2, 3],
                 [4]])

    def test_get_diagonal2(self):
        self.assertEqual(
                solution(
                        # matrix
                        [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]),
                # output
                [[1],
                 [2, 4],
                 [3, 5, 7],
                 [6, 8],
                 [9]])


if __name__ == '__main__':
    unittest.main()
