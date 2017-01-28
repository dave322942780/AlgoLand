import unittest
from random import randint

from pots_of_gold_dynamic import solution as dynamic_solution
from pots_of_gold_recursive import solution as recursive_solution


class BaseTestClass(object):
    class PotsOfGoldTestCase(unittest.TestCase):

        def setUp(self):
            self.solution = None

        def test_single(self):
            self.assertEqual(self.solution([3]), 3)

        def test_double(self):
            self.assertEqual(self.solution([7, 8]), 8)

        def test_many(self):
            for i in range(20):
                pots_of_gold = list(set([randint(0, 20) for i in range(randint(1, 30))]))
                if len(pots_of_gold) % 2 != 0:
                    pots_of_gold.pop()

                first_player = []
                second_player = []

                for i in range(len(pots_of_gold)):
                    # alternate terms
                    if i % 2 == 0:
                        res = self.solution(pots_of_gold)
                        if res == pots_of_gold[0]:
                            first_player.append(pots_of_gold.pop(0))
                        elif res == pots_of_gold[-1]:
                            first_player.append(pots_of_gold.pop())
                        else:
                            self.assertFalse("Number is not an option!")
                    else:
                        res = self.solution(pots_of_gold)
                        if res == pots_of_gold[0]:
                            second_player.append(pots_of_gold.pop(0))
                        elif res == pots_of_gold[-1]:
                            second_player.append(pots_of_gold.pop())
                        else:
                            self.assertFalse("Number is not an option!")
                self.assertTrue(sum(first_player) >= sum(second_player))


class PotsOfGoldDynamicTestCase(BaseTestClass.PotsOfGoldTestCase):
    def setUp(self):
        self.solution = dynamic_solution


class PotsOfGoldRecursiveTestCase(BaseTestClass.PotsOfGoldTestCase):
    def setUp(self):
        self.solution = recursive_solution
