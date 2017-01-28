# https://www.careercup.com/question?id=21263687
def solution(lst):
    lst = lst[:]
    for i in range(len(lst)):
        cur = lst[i]
        while cur is not None:
            idx = cur - 1
            new_cur = lst[idx]
            lst[idx] = None
            cur = new_cur
    res = []
    for i in range(len(lst)):
        if lst[i] is not None:
            res.append(i + 1)
    return res
