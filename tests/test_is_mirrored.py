import unittest

from data_structures_basic.Node import Node
from is_mirrored_tree import solution


class IsMirroredTreeTestCase(unittest.TestCase):
    def test_root(self):
        self.assertTrue(solution(Node(None)))

    def test_with_children_false(self):
        self.assertFalse(solution(
                Node.parse_tree("[[second_level_diff_1]"
                                       "root"
                                       "[second_level_diff_2]]")
        ))

        self.assertFalse(solution(
                Node.parse_tree("[[[third_level_structure_diff]second_level_same]"
                                       "root"
                                       "[[third_level_structure_diff]second_level_same]]")
        ))

        self.assertFalse(solution(
                Node.parse_tree("[[second_level_same[third_level_same[forth_level_diff_1]]]"
                                       "root"
                                       "[[[forth_level_diff_2]third_level_same]second_level_same]")
        ))

        self.assertFalse(solution(
                Node.parse_tree("[[[[forth_level_structure_diff]third_level_same]second_level_same]"
                                       "root"
                                       "[second_level_same[[forth_level_structure_diff]third_level_same]]]")

        ))

    def test_with_children_true(self):
        self.assertTrue(solution(
                Node.parse_tree("[[second_level_same]"
                                       "root"
                                       "[second_level_same]]")
        ))

        self.assertTrue(solution(
                Node.parse_tree("[[[third_level_same]second_level_same]"
                                       "root"
                                       "[second_level_same[third_level_same]]]")
        ))

        self.assertTrue(solution(
                Node.parse_tree("[[[third_level_same[forth_level_same]]second_level_same]"
                                       "root"
                                       "[second_level_same[[forth_level_same]third_level_same]]]")
        ))


if __name__ == '__main__':
    unittest.main()
