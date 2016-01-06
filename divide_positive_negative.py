
def solution(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            i += 1
        else:
            j = i + 1
            while i != j < len(lst):
                if lst[j] < 0:
                    elem = lst.pop(j)
                    lst.insert(i, elem)
                    i = j
                else:
                    j += 1