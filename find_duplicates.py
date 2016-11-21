# https://www.careercup.com/question?id=5719799180034048
# integers are in the range 0 <= x <= size of array

def solution(lst):
    for i in range(len(lst)):
        elem = lst[i]
        # None is visited, num is not, false if one occurrence, true is a duplicate
        if elem is None or type(elem) == bool:
            continue
        else:
            lst[i] = None
        while elem is not None:
            if type(lst[elem]) == bool:
                if not lst[elem]:
                    lst[elem], elem = True, None
                else:
                    elem = None
            else:
                lst[elem], elem = False, lst[elem]

    res = []
    for i in range(len(lst)):
        if lst[i]:
            res.append(i)

    return res
