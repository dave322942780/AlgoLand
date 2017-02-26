import unittest

from pos_neg_zip_zag import solution


class MyTestCase(unittest.TestCase):
    def test_general(self):
        self.assertEqual([-1, 5, -5, 9, -4, 7, -5, 3, -6, 7, -7, 2, -1],
                         solution([-1, 5, 9, 7, 3, -5, -4, 7, -5, -6, 2, -7, -1]))

        self.assertEqual([-1, 5, -6, 3, -7, -10],
                         solution([-1, -6, -7, 5, 3, -10]))
