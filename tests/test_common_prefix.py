import unittest

from common_prefix import solution


class MyTestCase(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEquals("iLove", solution(["iLoveDogs", "iLoveCats", "iLoveBunnies"]))
        self.assertEquals("iLike", solution(["iLike", "iLikeCats", "iLikeBunnies"]))
