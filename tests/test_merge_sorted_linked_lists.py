import unittest

from data_structures_basic.Node import Node
from merge_sorted_linked_lists import solution


class MyTestCase(unittest.TestCase):
    def test_merge_General(self):
        lst1 = Node([1, 3, 5, 9])
        lst2 = Node([2, 6, 8, 10])
        self.assertEqual(Node([1, 2, 3, 5, 6, 8, 9, 10]), solution(lst1, lst2))
