import unittest

from expand_to_0_and_1 import solution


class MyTestCase(unittest.TestCase):
    def test_no_replace(self):
        self.assertEqual(['abc'], solution("abc"))

    def test_replace_single(self):
        self.assertEqual({'a0b', 'a1b'}, set(solution("a?b")))

    def test_replace_general(self):
        self.assertEqual({'a0b0c', 'a0b1c', 'a1b0c', 'a1b1c'}, set(solution("a?b?c")))
        self.assertEqual({'a0bc0def0g', 'a0bc0def1g', 'a0bc1def0g',
                          'a0bc1def1g', 'a1bc0def0g', 'a1bc0def1g',
                          'a1bc1def0g', 'a1bc1def1g'}, set(solution("a?bc?def?g")))
