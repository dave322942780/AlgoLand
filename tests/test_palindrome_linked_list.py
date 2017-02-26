import unittest

from data_structures_basic.Node import Node
from palindrome_linked_list import solution


class MyTestCase(unittest.TestCase):
    def test_general(self):
        self.assertTrue(solution(Node([1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1])))
        self.assertTrue(solution(Node([1, 1])))
        self.assertTrue(solution(Node([1])))
        self.assertFalse(solution(Node([1, 2])))
        self.assertFalse(solution(Node([1, 2, 3])))
