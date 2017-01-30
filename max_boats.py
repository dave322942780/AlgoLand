# https://www.careercup.com/question?id=6303093824159744

def solution(weights, boat_capacity=150):
    weights.sort()
    if not weights:
        return 0
    elif weights[-1] > boat_capacity:
        raise Exception()
    i = 0
    j = len(weights) - 1
    count = 0
    while i <= j:
        if weights[i] + weights[j] <= boat_capacity:
            i += 1
        j -= 1
        count += 1
    return count
