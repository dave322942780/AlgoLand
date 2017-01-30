import unittest

from data_structures_basic.Node import Node
from reverse_linked_lst import solution


class MyTestCase(unittest.TestCase):
    def test_reverse_single(self):
        linked_lst = Node([1])
        linked_lst = solution(linked_lst)
        self.assertEqual(Node([1]), linked_lst)

    def test_reverse_general(self):
        linked_lst = Node([9, 2, 3, 4, 5])
        linked_lst = solution(linked_lst)
        expected_linked_lst = Node([5, 4, 3, 2, 9])
        self.assertEqual(expected_linked_lst, linked_lst)
