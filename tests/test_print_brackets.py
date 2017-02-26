import unittest

from print_brackets import solution


class MyTestCase(unittest.TestCase):
    def test_single(self):
        self.assertEqual({'(1)'}, set(solution([1])))

    def test_general(self):
        self.assertEqual({'(1234)', '(123)(4)', '(12)(34)', '(12)(3)(4)',
                          '(1)(234)', '(1)(23)(4)', '(1)(2)(34)', '(1)(2)(3)(4)'},
                         set(solution([1, 2, 3, 4])))
