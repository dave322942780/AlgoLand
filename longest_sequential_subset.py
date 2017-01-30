# https://www.careercup.com/question?id=11070934

def solution(lst):
    max_item = max(lst) + 1
    visited = [False] * max_item
    for item in lst:
        visited[item] = True
    max_seq = 0
    cur_max_seq = 0
    max_rang = None
    for i in range(len(visited)):
        item = visited[i]
        if item:
            cur_max_seq += 1
            if cur_max_seq > max_seq:
                max_seq = cur_max_seq
                max_rang = (i - cur_max_seq + 1, i + 1)
        else:
            cur_max_seq = 0

    return range(max_rang[0], max_rang[1])
