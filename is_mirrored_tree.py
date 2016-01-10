def _solution(left, right):
    if (not left and right) or (left and not right):
        return False
    elif not left and not right:
        return True
    else:
        return left.value == right.value and _solution(left.left, right.right) and _solution(left.right, right.left)


def solution(node):
    return _solution(node.left, node.right)
