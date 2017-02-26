# https://careercup.com/question?id=11532811

def solution(lst):
    min_left = lst[:]
    max_right = lst[:]

    for i in range(1, len(min_left)):
        min_left[i] = min(min_left[i - 1], min_left[i])

    for i in range(len(max_right) - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], max_right[i])

    i = j = 0

    max_range = 0
    max_range_indices = None

    while i < len(lst) and j < len(lst):
        if min_left[i] < max_right[j]:
            if (j - i) > max_range:
                max_range = j - i
                max_range_indices = i, j
            j += 1
        else:
            i += 1

    return max_range_indices
