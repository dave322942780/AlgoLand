import unittest

from data_structures_basic.BinaryNode import BinaryNode
from is_symmetric_tree import solution


class IsSymmeticTreeTestCase(unittest.TestCase):
    def test_root(self):
        self.assertTrue(solution(BinaryNode(None)))

    def test_with_children_false(self):
        self.assertFalse(solution(
                BinaryNode.parse_tree("[[second_level_diff_1]"
                                      "root"
                                      "[second_level_diff_2]]")
        ))

        self.assertFalse(solution(
                BinaryNode.parse_tree("[[[third_level_structure_diff]second_level_same]"
                                      "root"
                                      "[[third_level_structure_diff]second_level_same]]")
        ))

        self.assertFalse(solution(
                BinaryNode.parse_tree("[[second_level_same[third_level_same[forth_level_diff_1]]]"
                                      "root"
                                      "[[[forth_level_diff_2]third_level_same]second_level_same]")
        ))

        self.assertFalse(solution(
                BinaryNode.parse_tree("[[[[forth_level_structure_diff]third_level_same]second_level_same]"
                                      "root"
                                      "[second_level_same[[forth_level_structure_diff]third_level_same]]]")

        ))

    def test_with_children_true(self):
        self.assertTrue(solution(
                BinaryNode.parse_tree("[[second_level_same]"
                                      "root"
                                      "[second_level_same]]")
        ))

        self.assertTrue(solution(
                BinaryNode.parse_tree("[[[third_level_same]second_level_same]"
                                      "root"
                                      "[second_level_same[third_level_same]]]")
        ))

        self.assertTrue(solution(
                BinaryNode.parse_tree("[[[third_level_same[forth_level_same]]second_level_same]"
                                      "root"
                                      "[second_level_same[[forth_level_same]third_level_same]]]")
        ))


if __name__ == '__main__':
    unittest.main()
