import unittest

from k_palindrome import solution


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(solution("ww", 0))
        self.assertFalse(solution("wwr", 0))

    def test_one(self):
        self.assertTrue(solution("wwr", 1))
        self.assertTrue(solution("rwr", 0))

    def test_many(self):
        self.assertTrue(solution("wwr", 1))
        self.assertFalse(solution("3wwr4", 2))
        self.assertTrue(solution("3w4r4", 2))
