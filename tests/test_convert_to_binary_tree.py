import unittest

from convert_to_binary_tree import solution
from data_structures_basic.BinaryNode import BinaryNode


class MyTestCase(unittest.TestCase):
    def test_common_prefix(self):
        sol = BinaryNode.parse_tree("[[1[[2]4[5]]]6[7]]", int)
        self.assertEqual(sol, solution(BinaryNode.parse_tree("[[5[[6]4[1]]]2[7]]", int)))
