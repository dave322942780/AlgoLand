import unittest

from unscramble_words import solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.words = open("./words.txt").read()

    def test_single(self):
        # stock entertain
        self.assertEqual({'stock'},
                         set(solution(self.words.replace("\n", " ").split(" "), "otkcs")))

    def test_general(self):
        # stock entertain
        self.assertEqual({'entertain', 'stock'},
                         set(solution(self.words.replace("\n", " ").split(" "), "nreoctaistentk")))
        # stock stock vain
        self.assertEqual(sorted(['vain', 'stock', 'stock']),
                         sorted(solution(self.words.replace("\n", " ").split(" "), "vocktoaisstckn")))
