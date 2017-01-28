import unittest

from bomber import solution


class MyTestCase(unittest.TestCase):
    def test_base(self):
        self.assertEqual(solution([[1]]), (0, 0))

    def test_big_map(self):
        self.assertEqual(solution([[1, 0],
                                   [1, 1]]
                                  ), (0, 1))

    def test_big_big_map(self):
        self.assertEqual(solution([[1, 0, 1],
                                   [1, 1, 1],
                                   [1, 0, 0]]
                                  ), (0, 1))
