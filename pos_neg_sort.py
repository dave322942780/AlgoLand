# https://careercup.com/question?id=5201559730257920

def solution(lst):
    for i in range(len(lst) - 1):
        if lst[i] > 0 and lst[i + 1] < 0:
            j = i
            while j > 0 and lst[j] > 0:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                j -= 1
    return lst
