import unittest

from maximum_area_covered import solution


def island_to_matrix(island):
    return map(lambda x: map(lambda y: 1 if y == "o" else 0, list(x)), island.strip("\n").split("\n"))


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        island = \
            "          \n" + \
            "          \n" + \
            "          \n" + \
            "          \n"

        self.assertEqual(0, solution(island_to_matrix(island)))

    def test_single_island(self):
        island = \
            "ooooo\n" + \
            "oo  o\n" + \
            "ooooo\n"

        self.assertEqual(13, solution(island_to_matrix(island)))

    def test_general(self):
        island = \
            "                    \n" + \
            "      o             \n" + \
            "o   ooooo           \n" + \
            " o   o  o   o       \n" + \
            "o oooo  o   oooo    \n" + \
            "ooo  ooo oo oooooo  \n" + \
            "                    \n" + \
            "     oo         ooo \n" + \
            "            o       \n" + \
            "         o          \n" + \
            "                    \n"

        self.assertEqual(20, solution(island_to_matrix(island)))
