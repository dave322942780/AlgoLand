# https://careercup.com/question?id=4748947486670848

def solution(lst):
    pos = filter(lambda x: x > 0, lst)
    neg = filter(lambda x: x < 0, lst)
    i = j = k = 0
    while i < len(pos) and j < len(neg) and k < len(lst):
        # odd
        if k % 2:
            lst[k] = pos[i]
            i += 1
        else:
            lst[k] = neg[j]
            j += 1
        k += 1

    remaining = neg[j:] if j < len(neg) else pos[j:]
    for i in range(len(lst) - 1, len(lst) - len(remaining) - 1, -1):
        lst[i] = remaining.pop()
    return lst
