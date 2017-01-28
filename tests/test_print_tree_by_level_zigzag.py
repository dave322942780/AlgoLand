import unittest

from data_structures_basic.BinaryNode import BinaryNode
from print_tree_by_level_zigzag import solution


class MyTestCase(unittest.TestCase):
    def test_single_node(self):
        node = BinaryNode(1)


    def test_binary_tree(self):
        tree = BinaryNode.parse_tree("[[[3]2[[5]4]]1[[3[6]]8[9]]]", int)
        self.assertEqual("128934356", solution(tree))

    def test_binary_tree_2(self):
        tree = BinaryNode.parse_tree("[[[5]3[4]]5[[6]3[[4]2[8[9]]]]]", int)
        self.assertEqual("5332645489", solution(tree))