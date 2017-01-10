import unittest

from find_missing_number import solution


class MyTestCase(unittest.TestCase):
    def test_find_missing_numbers1(self):
        lst = [2, 5, 6, 6, 3, 1, 2, 1]
        self.assertEqual(solution(lst), [4, 7, 8])
