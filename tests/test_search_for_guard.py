import unittest

from search_for_guard import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        lsts = [[0, 0, 0],
                ["B", "G", "G"],
                ["B", 0, 0]]
        sol = [[2, 1, 1],
               ["B", "G", "G"],
               ["B", 1, 1]]
        self.assertEqual(solution(lsts), sol)


if __name__ == '__main__':
    unittest.main()
