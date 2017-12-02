import unittest

from jump_game_2 import Solution


class MyTestCase(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(2, Solution().jump([2,3,1,1,4]))