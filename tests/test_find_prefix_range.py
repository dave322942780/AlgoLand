import unittest

from find_prefix_range import solution


class PrefixRangeTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual((0, 0), solution(["aa", "bb"], "a"))

    def test_two(self):
        self.assertEqual((0, 1), solution(["aa", "ab"], "a"))

    def test_big_map(self):
        self.assertEqual((4,6),solution(["aa", "aa", "abb", "abc", "acc", "acd", "ace"], "ac"))

    def test_big_big_map(self):
        try:
            solution(["aa", "ab"], "b")
            self.fail("not found, exception not raised")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
