import unittest

from string_permutation import solution


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual({''}, set(solution('')))

    def test_single(self):
        self.assertEqual({'', 'a'}, set(solution('a')))

    def test_general(self):
        self.assertEqual({'abc', 'bc', 'ac', 'c', 'ab', 'b', 'a', ''}, set(solution("abc")))
