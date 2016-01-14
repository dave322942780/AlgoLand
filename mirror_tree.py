def solution(node):
    if node:
        tmp = node.right
        node.right = node.left
        node.left = tmp
        solution(node.left)
        solution(node.right)
