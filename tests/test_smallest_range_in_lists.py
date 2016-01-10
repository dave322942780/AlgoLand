import unittest

from smallest_range_in_lists import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        lsts = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        self.assertEqual(solution(lsts), (20, 24))


if __name__ == '__main__':
    unittest.main()
