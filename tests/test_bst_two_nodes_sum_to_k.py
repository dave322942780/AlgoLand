import unittest

from bst_two_nodes_sum_to_k import solution
from data_structures_basic.BinaryNode import BinaryNode


class MyTestCase(unittest.TestCase):

    def test_many(self):
        tree = BinaryNode.parse_tree("[[1[[5]3[4]]]5[6[11]]]", int)
        sol = solution(tree, 10)
        self.assertEqual(10, sol[0].value + sol[1].value)

    def test_no_sol(self):
        tree = BinaryNode.parse_tree("[[1[[5]3[4]]]5[6[12]]]", int)
        sol = solution(tree, 12)
        self.assertIsNone(sol)

