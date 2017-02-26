import unittest

from without_operators import no_multiply_op, no_add_op, no_exponent_op


class MyTestCase(unittest.TestCase):
    def test_no_multiply_op(self):
        self.assertEqual(12, no_multiply_op(3, 4))
        self.assertEqual(12, no_multiply_op(4, 3))
        self.assertEqual(30, no_multiply_op(5, 6))
        self.assertEqual(24, no_multiply_op(6, 4))
        self.assertEqual(36, no_multiply_op(6, 6))

    def test_no_add_op(self):
        self.assertEqual(5, no_add_op(2, 3))
        self.assertEqual(11, no_add_op(8, 3))
        self.assertEqual(12, no_add_op(7, 5))

    def test_no_exponent_op(self):
        self.assertEqual(8, no_exponent_op(2, 3))
        self.assertEqual(16, no_exponent_op(2, 5))
        self.assertEqual(196, no_exponent_op(7, 5))
