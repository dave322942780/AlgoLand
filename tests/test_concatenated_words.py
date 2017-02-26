import unittest

from concatenated_words import solution


class MyTestCase(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual([['hello', 'world']], solution("helloworld", ["hello", "world", "super", "hell"]))
        self.assertEqual([], solution("superman", ["hello", "world", "super", "hell"]))
        self.assertEqual([['hello', 'hello']], solution("hellohello", ["hello", "world", "super", "hell"]))
