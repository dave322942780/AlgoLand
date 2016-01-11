# http://www.careercup.com/question?id=21263687

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

    for num in lst:
        if 1 << i & num == 0:
            res1 ^= num
        else:
            res2 ^= num

    return res1, res2
