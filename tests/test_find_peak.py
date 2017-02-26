import unittest

from find_peak import solution


class MyTestCase(unittest.TestCase):
    def test_find_peak(self):
        self.assertEqual(6, solution([2, 3, 4, 5, 6, 7, 10, 9, 8, 7]))
