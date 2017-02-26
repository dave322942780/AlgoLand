import unittest

from find_freetime import solution


class MyTestCase(unittest.TestCase):
    def test_find_freetime(self):
        self.assertEqual([(6, 10), (14, 15), (21, 25)], solution(
            [[[1, 5], [10, 14], [19, 20], [27, 30]],
             [[3, 6], [13, 14], [15, 21], [27, 31]],
             [[0, 2], [12, 13], [25, 28]],
             [[2, 4], [27, 30]]]))
