# https://www.careercup.com/question?id=5094709806497792

def solution(lst):
    hashed_counts = [0, ] * len(lst)
    for i in lst:
        if i >= len(lst):
            i = len(lst) - 1
        elif i < 0:
            i = 0
        hashed_counts[i] += 1
    accumulator = 0
    for i in range(len(hashed_counts) - 1, -1, -1):
        accumulator += hashed_counts[i]
        if accumulator >= i:
            return i
