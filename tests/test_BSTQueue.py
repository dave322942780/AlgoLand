import unittest

from data_structures_basic.BSTQueue import MinBSTQueue
from data_structures_basic.BSTQueue import BinaryNode


class MyBSTQueue(unittest.TestCase):
    def test_one_node(self):
        min_bst_queue = MinBSTQueue(BinaryNode.parse_tree("[1]", int))
        self.assertEqual(min_bst_queue.get().value, 1)

    def test_no_left(self):
        binary_tree = BinaryNode.parse_tree("[1[2]]", int)
        min_bst_queue = MinBSTQueue(binary_tree)
        self.assertEqual(min_bst_queue.get().value, 1)
        self.assertEqual(min_bst_queue.get().value, 2)

    def test_no_right(self):
        min_bst_queue = MinBSTQueue(BinaryNode.parse_tree("[[1]2]", int))
        self.assertEqual(min_bst_queue.get().value, 1)
        self.assertEqual(min_bst_queue.get().value, 2)

    def test_int(self):
        min_bst_queue = MinBSTQueue(BinaryNode.parse_tree("[[1[[2]3[4]]]5[6]]", int))
        self.assertEqual(min_bst_queue.get().value, 1)
        self.assertEqual(min_bst_queue.get().value, 2)
        self.assertEqual(min_bst_queue.get().value, 3)
        self.assertEqual(min_bst_queue.get().value, 4)
        self.assertEqual(min_bst_queue.get().value, 5)
        self.assertEqual(min_bst_queue.get().value, 6)


if __name__ == '__main__':
    unittest.main()
