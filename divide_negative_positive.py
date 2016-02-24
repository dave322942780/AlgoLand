# http://www.careercup.com/question?id=19286747
# Given an array of integers. Find two disjoint contiguous sub-arrays such
# that the absolute difference between the sum of two sub-array is maximum.
# * The sub-arrays should not overlap.
# eg- [2 -1 -2 1 -4 2 8] ans - (-1 -2 1 -4) (2 8), diff = 16
# I gave him o(n^2) algorithm but he was not satisfied.

def solution(lst):
    i = 0
    j = 0
    while i < len(lst) and j < len(lst):
        if lst[i] < 0:
            i += 1
        else:
            j = i + 1
            while j < len(lst):
                if lst[j] < 0:
                    elem = lst.pop(j)
                    lst.insert(i, elem)
                    break
                else:
                    j += 1
