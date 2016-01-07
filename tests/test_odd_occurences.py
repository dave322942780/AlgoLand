import unittest
from find_odd_occurances import solution


class OddOccurrencesTestCase(unittest.TestCase):
    def test_many(self):
        lst = [4, 44, 55, 8, 44, 7, 55, 7, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 3, 4, 5, 5, 4, 3]
        res = solution(lst)
        self.assertEqual(len(res), 2)
        self.assertIn(4, res)
        self.assertIn(8, res)
