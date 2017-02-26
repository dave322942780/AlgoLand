# https://careercup.com/question?id=5737503739871232

def solution(lst):
    assert len(lst) >= 3

    i = 0
    j = len(lst) - 1
    mid = (i + j) / 2
    while not lst[mid - 1] < lst[mid] > lst[mid + 1]:
        if lst[mid - 1] < lst[mid]:
            i = mid
        else:
            j = mid
        mid = (i + j) / 2
    return mid
