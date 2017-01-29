import unittest

from push_zeros_to_end import solution


class MyTestCase(unittest.TestCase):
    def test_no_action(self):
        input_param = [1, 4, 8, 9, 0, 0, 0, 0, 0, 0]
        expected_res = input_param[:]
        solution(input_param)
        self.assertEqual(expected_res, input_param)

    def test_general(self):
        input_param = [1, 0, 0, 4, 0, 8, 0, 0, 0, 9]
        solution(input_param)
        self.assertEqual([1, 4, 8, 9, 0, 0, 0, 0, 0, 0], input_param)
