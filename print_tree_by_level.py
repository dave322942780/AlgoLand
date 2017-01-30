# https://www.careercup.com/question?id=5389078581215232

def solution(tree):
    nodes_by_level = []

    def _solution(node, level):
        if not node:
            return
        else:
            if len(nodes_by_level) == level:
                nodes_by_level.append([])
            nodes_by_level[level].append(str(node.value))
            _solution(node.left, level + 1)
            _solution(node.right, level + 1)

    _solution(tree, 0)
    nodes_by_level.reverse()

    return "".join(["".join(level) for level in nodes_by_level])
