# http://www.careercup.com/question?id=15320677

def _flatten(node):
    if node is None:
        return []
    else:
        return _flatten(node.left) + [node] + _flatten(node.right)


def solution(node, k):
    node_lst_format = _flatten(node)
    i = 0
    j = len(node_lst_format) - 1
    while i < j:
        i_j_sum = node_lst_format[j].value + node_lst_format[i].value
        if i_j_sum == k:
            return node_lst_format[i], node_lst_format[j]
        elif i_j_sum > k:
            j -= 1
        elif i_j_sum < k:
            i += 1
    return None
