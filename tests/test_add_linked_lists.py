import unittest

from add_linked_lists import solution
from data_structures_basic.Node import Node


class MyTestCase(unittest.TestCase):
    def test_add_general(self):
        lst1 = Node([9, 2, 3, 4, 5])
        lst2 = Node([8, 2, 5, 8])
        expected_res = Node([1, 0, 0, 6, 0, 3])
        lst_sum = solution(lst1, lst2)
        self.assertEqual(expected_res, lst_sum)

        lst_sum = solution(lst1, lst2)
        self.assertEqual(expected_res, lst_sum)
