import unittest

from data_structures_basic.BinaryNode import BinaryNode
from merge_bst import solution


class MyTestCase(unittest.TestCase):
    def test_general(self):
        def flatten(node):
            if node:
                return flatten(node.left) + [node.value] + flatten(node.right)
            else:
                return []

        bst1 = BinaryNode.parse_tree("[[1[[3]5[7]]]9[17]]", int)
        bst2 = BinaryNode.parse_tree("[[[2]4[[6]8]]10[[12[16]]18]]", int)
        merged = solution(bst1, bst2)

        flt1 = flatten(bst1)
        flt2 = flatten(bst2)

        self.assertEqual(sorted(flt1 + flt2), flatten(merged))
