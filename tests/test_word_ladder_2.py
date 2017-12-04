import unittest

from word_ladder_2 import Solution


class MyTestCase(unittest.TestCase):
    def test_word_ladder_2(self):
        self.assertEquals(sorted([["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]),
                          sorted(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])))
