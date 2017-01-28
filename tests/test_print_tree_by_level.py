import unittest

from data_structures_basic.BinaryNode import BinaryNode
from print_tree_by_level import solution


class MyTestCase(unittest.TestCase):
    def test_single_node(self):
        node = BinaryNode(1)
        self.assertEqual(str(node.value), solution(node))

    def test_binary_tree(self):
        tree = BinaryNode.parse_tree("[[[3]2[[5]4]]1[[4[5]]2[3]]]", int)
        self.assertEqual("553443221", solution(tree))

    def test_complete_binary_tree(self):
        tree = BinaryNode.parse_tree("[[[5]3[4]]5[[6]12[2]]]", int)
        self.assertEqual("54623125", solution(tree))
