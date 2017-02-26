import unittest

from check_is_perfect_squre import solution


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution(1))
        self.assertTrue(solution(4))
        self.assertTrue(solution(9))
        self.assertTrue(solution(16))
        self.assertTrue(solution(10000))

    def test_False(self):
        self.assertFalse(solution(15))
        self.assertFalse(solution(9999))
        self.assertFalse(solution(26243))
        self.assertFalse(solution(245))
        self.assertFalse(solution(678))
