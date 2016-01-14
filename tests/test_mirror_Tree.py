import unittest

from data_structures_basic.BinaryNode import BinaryNode
from mirror_tree import solution


class MirrorTreeTestCase(unittest.TestCase):
    def test_non_symmetric_tree(self):
        tree = BinaryNode.parse_tree("[[1[[2]3[4]]]5]", int)
        solution(tree)
        tree2 = BinaryNode.parse_tree("[5[[[4]3[2]]1]]", int)
        self.assertEqual(tree, tree2)

    def test_symmetric_tree(self):
        tree = BinaryNode.parse_tree("[[[3]2[[5]4]]1[[4[5]]2[3]]]", int)
        solution(tree)
        tree2 = BinaryNode.parse_tree("[[[3]2[[5]4]]1[[4[5]]2[3]]]", int)
        self.assertEqual(tree, tree2)


if __name__ == '__main__':
    unittest.main()
