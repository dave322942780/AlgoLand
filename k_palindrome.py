# http://www.careercup.com/question?id=6287528252407808
# difficulty: easy
# category: recursion


def solution(word, k):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return solution(word[1:], k - 1) or solution(word[:-1], k - 1)
    else:
        return solution(word[1:-1], k)
