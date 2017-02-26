# https://careercup.com/question?id=5699311095513088


def solution(tree):
    elem_values = []

    def get_values(node, values):
        if node:
            values.append(node.value)
            node.value = None
            get_values(node.left, values)
            get_values(node.right, values)

    def insert(node, values):
        if node:
            insert(node.right, values)
            node.value = values.pop()
            insert(node.left, values)

    get_values(tree, elem_values)
    elem_values.sort()
    insert(tree, elem_values)
    return tree
