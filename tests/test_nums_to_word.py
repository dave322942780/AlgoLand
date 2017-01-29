import unittest

from num_to_word import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letter in enumerate(letters):
            actual_res = solution(i)
            self.assertIn(letter, actual_res)

    def test_multiple(self):
        self.assertEqual({'abc', 'aw', 'lc'}, set(solution(123)))
        self.assertEqual({'cab', 'cl', 'Eb'}, set(solution(312)))
        self.assertEqual({'fgh'}, set(solution(678)))
        self.assertEqual({'egcbd', 'egcx', 'egFd'}, set(solution(57324)))
