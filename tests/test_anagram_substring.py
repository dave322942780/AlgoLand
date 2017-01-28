# https://careercup.com/question?id=19286747
import unittest

from anagram_substring import solution


class MyTestCase(unittest.TestCase):
    def test_anagram_substring(self):
        self.assertTrue(solution("aabc", "adsgbaacariojgw"))

    def test_anagram_substring2(self):
        self.assertFalse(solution("aabc", "adsgbacriojgw"))

    def test_anagram_substring3(self):
        self.assertTrue(solution("a", "adsgbaacariojgw"))
