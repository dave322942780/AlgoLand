# https://careercup.com/question?id=5733590840115200
from data_structures_basic.BinaryNode import BinaryNode


def solution(bst1, bst2):
    def extract_to_lst(node, abc):
        if node:
            extract_to_lst(node.right, abc)
            abc.append(node.value)
            extract_to_lst(node.left, abc)
        return abc

    values = []
    values1 = extract_to_lst(bst1, [])
    values2 = extract_to_lst(bst2, [])

    while values1 or values2:
        if values1 and values2:
            if values1[-1] < values2[-1]:
                values.append(values1.pop())
            else:
                values.append(values2.pop())
        elif values1:
            values.append(values1.pop())
        elif values2:
            values.append(values2.pop())

    def insert_to_tree(lst, i, j):
        if i <= j:
            mid = (i + j) / 2
            return BinaryNode(lst[mid], insert_to_tree(lst, i, mid - 1), insert_to_tree(lst, mid + 1, j))

    return insert_to_tree(values, 0, len(values) - 1)
