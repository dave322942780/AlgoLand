# https://careercup.com/question?id=7617672


def solution(tree):
    def _solution(node, path):
        if node and node.value == 1:
            path.append(node)
            left = _solution(node.left, path)
            right = _solution(node.right, path)
            longest_path = None
            for cur_path in (left, right, path[:]):
                if cur_path and (not longest_path or len(cur_path) > len(longest_path)):
                    longest_path = cur_path
            path.remove(node)
            return longest_path

    return _solution(tree, [])
