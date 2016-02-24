# http://www.careercup.com/question?id=21263687
# You are given an array of n integers which can contain integers from 1 to n only.
# Some elements can be repeated multiple times and some other elements can be absent
# from the array . Write a running code on paper which takes O(1) space apart from
# the input array and O(n) time to print which elements are not present in the array
# and the count of every element which is there in the array along with the element number . 
# 
# NOTE: The array isn't necessarily  sorted.

def solution(lst):
    xor_product = 0
    # xor all the bits to get the xor'd product of the two odd occurrence words
    for i in lst:
        xor_product ^= i

    # find out at which bit they are different
    i = 0
    while 1 << i & xor_product == 0:
        i += 1

    res1 = 0
    res2 = 0

    # xor 2 type of numbers separately, one with ith bit equal to 0,
    # one with ith bit equal to equals to 1. The 2 results are excatly the
    # 2 numbers.
    for num in lst:
        if 1 << i & num == 0:
            res1 ^= num
        else:
            res2 ^= num

    return res1, res2
