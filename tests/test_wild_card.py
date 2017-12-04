import unittest

from wild_card import Solution


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertFalse(Solution().isMatch("b", "?*?"))

    def test1(self):
        self.assertFalse(Solution().isMatch("zacabz", "*a?b*"))

    def test2(self):
        self.assertFalse(Solution().isMatch("aa", "a"))

    def test3(self):
        self.assertTrue(Solution().isMatch("aa", "*"))

    def test4(self):
        self.assertFalse(Solution().isMatch("a", "aa"))


    def test5(self):
        self.assertTrue(Solution().isMatch("a", "*a*"))