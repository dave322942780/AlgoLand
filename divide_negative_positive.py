# http://www.careercup.com/question?id=19286747


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
