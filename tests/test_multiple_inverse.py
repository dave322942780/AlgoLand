import unittest

from multiply_inverse import solution


class MultipleInverseTestCase(unittest.TestCase):
    def test_multiple_inverse(self):
        self.assertEqual([24, 12, 8, 6], solution([1, 2, 3, 4]))
