import unittest

from interleaves import solution_gen_interleaves
from interleaves import solution_test_interleave


class MyTestCase(unittest.TestCase):
    def test_is_interleave_single(self):
        self.assertTrue(solution_test_interleave("a", "b", "ab"))
        self.assertTrue(solution_test_interleave("a", "b", "ba"))

    def test_is_interleave_empty(self):
        self.assertFalse(solution_test_interleave("", "b", ""))
        self.assertFalse(solution_test_interleave("a", "", ""))
        self.assertFalse(solution_test_interleave("a", "b", ""))

        self.assertTrue(solution_test_interleave("", "b", "b"))
        self.assertTrue(solution_test_interleave("a", "", "a"))
        self.assertTrue(solution_test_interleave("", "", ""))

    def test_is_interleave_true(self):
        self.assertTrue(solution_test_interleave("abdd", "cbe", "acbbded"))
        self.assertTrue(solution_test_interleave("abd", "cbe", "acbbde"))
        self.assertTrue(solution_test_interleave("abd", "cbe", "cabbde"))

    def test_is_interleave_false(self):
        self.assertFalse(solution_test_interleave("abdd", "cbe", "acbbde"))
        self.assertFalse(solution_test_interleave("abd", "cbe", "acbdeb"))

    def test_gen_interleaves(self):
        self.assertEqual(set(solution_gen_interleaves("A", "CD")), {'ACD', 'CAD', 'CDA'})
        self.assertEqual(set(solution_gen_interleaves("AB", "CD")),
                         {'ABCD', 'ACBD', 'ACDB', 'CABD', 'CADB', 'CDAB'})
        self.assertEqual(set(solution_gen_interleaves("AB", "CDE")),
                         {'ABCDE', 'ACBDE', 'ACDBE', 'ACDEB', 'CABDE', 'CADBE', 'CADEB', 'CDABE', 'CDAEB', 'CDEAB'})
