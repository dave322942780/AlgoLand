# http://www.careercup.com/question?id=15422849

def _solution(lst, start, end, semantic_array):
    if semantic_array[start][end]:
        return semantic_array[start][end]
    if start < end - 2:
        skip_edges = _solution(lst, start + 1, end - 1, semantic_array)
        left = lst[start] + min([_solution(lst, start + 2, end, semantic_array), skip_edges])
        right = lst[end - 1] + min([skip_edges, _solution(lst, start, end - 2, semantic_array)])
        semantic_array[start][end] = lst[start] if left == max(left, right) else lst[end - 1]
    elif start == end - 1:
        semantic_array[start][end] = lst[start]
    elif start == end - 2:
        semantic_array[start][end] = max(lst[start], lst[end - 1])
    return semantic_array[start][end]


def solution(lst):
    length = len(lst)
    return _solution(lst, 0, length, [[None] * (length + 1)] * (length + 1))
