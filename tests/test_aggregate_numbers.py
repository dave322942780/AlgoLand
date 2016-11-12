import unittest

from aggregate_numbers import solution


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution("112358"))
        self.assertTrue(solution("122436"))
        self.assertTrue(solution("1299111210"))
        self.assertTrue(solution("112112224"))

    def test_false(self):
        self.assertFalse(solution("234526"))
        self.assertFalse(solution("3567"))
        self.assertFalse(solution("47456"))
        self.assertFalse(solution("112354"))
