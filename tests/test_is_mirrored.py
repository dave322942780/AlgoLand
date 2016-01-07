import unittest
from is_mirrored_tree import solution
from objects.Node import Node


class IsMirroredTreeTestCase(unittest.TestCase):
    def test_root(self):
        self.assertTrue(solution(Node(None)))

    def test_with_children_false(self):
        self.assertFalse(solution(
                Node("root",
                     Node("second_level_diff_1"),
                     Node("second_level_diff_2"))))

        self.assertFalse(solution(
                Node("root",
                     Node("second_level_same",
                          Node("third_level_structure_diff"),
                          None
                          ),
                     Node("second_level_same",
                          Node("third_level_structure_diff"),
                          None
                          )
                     )
        ))

        self.assertFalse(solution(
                Node("root",
                     Node("second_level_same",
                          Node("third_level_same",
                               Node("forth_level_diff_1"),
                               None
                               ),
                          None
                          ),
                     Node("second_level_same",
                          None,
                          Node("third_level_same",
                               None,
                               Node("forth_level_diff_2")
                               )
                          )
                     )
        ))

        self.assertFalse(solution(
                Node("root",
                     Node("second_level_same",
                          Node("third_level_same",
                               Node("forth_level_structure_diff"),
                               None
                               ),
                          None
                          ),
                     Node("second_level_same",
                          None,
                          Node("third_level_same",
                               Node("forth_level_structure_diff"),
                               None
                               )
                          )
                     )
        ))

    def test_with_children_true(self):
        self.assertTrue(solution(
                Node("root",
                     Node("second_level_same"),
                     Node("second_level_same"))))

        self.assertTrue(solution(
                Node("root",
                     Node("second_level_same",
                          None,
                          Node("third_level_same")
                          ),
                     Node("second_level_same",
                          Node("third_level_same"),
                          None
                          )
                     )
        ))

        self.assertTrue(solution(
                Node("root",
                     Node("second_level_same",
                          Node("third_level_same",
                               Node("forth_level_same"),
                               None
                               ),
                          None
                          ),
                     Node("second_level_same",
                          None,
                          Node("third_level_same",
                               None,
                               Node("forth_level_same")
                               )
                          )
                     )
        ))
