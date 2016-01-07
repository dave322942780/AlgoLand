def _solution(lst, start, end, semantic_array):
    if start < end - 2:
        if semantic_array[start - 1][end - 1] is not None:
            return semantic_array[start - 1][end - 1]
        left = lst[start] + min([_solution(lst, start + 2, end, semantic_array),
                                 _solution(lst, start + 1, end - 1, semantic_array)])
        right = lst[end - 1] + min([_solution(lst, start + 1, end - 1, semantic_array),
                                    _solution(lst, start, end - 2, semantic_array)])
        semantic_array[start - 1][end - 1] = lst[start] if left == max(left, right) else lst[end - 1]
        return semantic_array[start - 1][end - 1]
    elif start == end - 1:
        return lst[start]
    elif start == end - 2:
        return max(lst[start], lst[end - 1])


def solution(lst):
    return _solution(lst, 0, len(lst), [[None] * len(lst)] * len(lst))
