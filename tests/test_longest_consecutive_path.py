import unittest

from data_structures_basic.BinaryNode import BinaryNode
from longest_consecutive_path import solution


class MyTestCase(unittest.TestCase):
    def test_general(self):
        bst = BinaryNode.parse_tree("[[1[[2]3[4]]]5[6]]", int)
        node, is_left = solution(bst)
        self.assertEqual(bst.left, node)
        self.assertFalse(is_left)

        bst = BinaryNode.parse_tree("[[1[2[3[4[5]]]]]6[5[4[3[2]]]]]", int)
        node, is_left = solution(bst)
        self.assertEqual(bst.left, node)
        self.assertFalse(is_left)
