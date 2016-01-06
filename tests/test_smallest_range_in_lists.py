import unittest
from smallest_range_in_lists import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        lst = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        solution(lst)


if __name__ == '__main__':
    unittest.main()
