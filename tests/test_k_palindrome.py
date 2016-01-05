import unittest
import k_palindrome


class KPalindromeTestCase(unittest.TestCase):

    def test_zero(self):
        self.assertTrue(k_palindrome.solution("ww", 0))
        self.assertFalse(k_palindrome.solution("wwr", 0))

    def test_one(self):
        self.assertTrue(k_palindrome.solution("wwr", 1))
        self.assertTrue(k_palindrome.solution("rwr", 0))

    def test_many(self):
        self.assertTrue(k_palindrome.solution("wwr", 1))
        self.assertFalse(k_palindrome.solution("3wwr4", 2))
        self.assertTrue(k_palindrome.solution("3w4r4", 2))


if __name__ == '__main__':
    unittest.main()
