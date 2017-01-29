import unittest

from data_structures_basic.BinaryNode import BinaryNode
from deepest_1_path import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        tree = BinaryNode.parse_tree("[1]", int)
        self.assertEqual([tree], solution(tree))

    def test_all_ones(self):
        tree = BinaryNode.parse_tree("[[1[1]]1[1]]", int)
        self.assertEqual([tree, tree.left, tree.left.right], solution(tree))

    def test_zero_leaves(self):
        tree = BinaryNode.parse_tree("[1[[1[0]]1[0]]]", int)
        self.assertEqual([tree, tree.right, tree.right.left], solution(tree))

    def test_zero_intermediate_node(self):
        tree = BinaryNode.parse_tree("[[0[1]]1[[0]1[[1]0[1]]]]]", int)
        self.assertEqual([tree, tree.right], solution(tree))
