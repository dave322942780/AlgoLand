import unittest

from text_justification import Solution


class MyTestCase(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(["This    is    an",
   "example  of text",
   "justification.  "
], Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))