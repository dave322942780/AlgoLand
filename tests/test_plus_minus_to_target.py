import unittest

from plus_minus_to_target import solution


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(set(), set(solution([2, 4, 6, 8], 22)))

    def test_single(self):
        actual_res = solution([2, 4, 6, 8], 20)
        self.assertEqual(1, len(actual_res))
        self.assertEqual([1, 1, 1, 1], actual_res[0])

    def test_multi(self):
        actual_res = solution([2, 4, 6, 8], 12)
        expected_res = [[1, 1, 1, 0], [1, -1, 1, 1], [0, 1, 0, 1], [-1, 0, 1, 1]]
        self.assertTrue(len(actual_res), len(expected_res))
        for lst1 in expected_res:
            test_in = False
            for lst2 in actual_res:
                if lst1 == lst2:
                    test_in = True
                    break
            if not test_in:
                self.assertTrue(test_in)
