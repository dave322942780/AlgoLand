# https://careercup.com/question?id=19286747
import unittest

from longest_sequential_subset import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        self.assertTrue([5], solution(solution([5])))

    def test_anagram_substring2(self):
        self.assertFalse(solution("aabc", "adsgbacriojgw"))

    def test_anagram_substring3(self):
        self.assertTrue(solution("a", "adsgbaacariojgw"))
