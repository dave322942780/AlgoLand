# http://www.careercup.com/question?id=6287528252407808
# difficulty: 2
# length: 3


def solution(word, k):

    if k < 0:
        return False
    elif len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return solution(word[1:], k - 1) or solution(word[:-1], k - 1)
    else:
        return solution(word[1:-1], k)

