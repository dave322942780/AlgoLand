import unittest

from bst_two_nodes_sum_to_k import solution
from data_structures_basic.BinaryNode import Node


class NodesSumToKTestCase(unittest.TestCase):
    def test_many(self):
        tree = Node.parse_tree("[[1[[2]3[4]]]5[6]]", int)
        sol = solution(tree, 10)
        self.assertEqual(10, sol[0].value + sol[1].value)


if __name__ == '__main__':
    unittest.main()
