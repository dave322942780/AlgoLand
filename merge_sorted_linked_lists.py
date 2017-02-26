# https://careercup.com/question?id=5702478461927424

from data_structures_basic.Node import Node


def solution(lst1, lst2):
    cur1 = lst1
    cur2 = lst2

    head = Node("Dummy")
    cur = head

    while cur1 and cur2:
        if cur1.value < cur2.value:
            cur.next_node = Node(cur1.value)
            cur1 = cur1.next_node
        else:
            cur.next_node = Node(cur2.value)
            cur2 = cur2.next_node
        cur = cur.next_node
    left_over = cur1 if cur1 else cur2

    while left_over:
        cur.next_node = Node(left_over.value)
        cur = cur.next_node
        left_over = left_over.next_node

    return head.next_node
