from data_structures_basic.Node import Node


def solution(lst1, lst2):
    def _add_lsts(lst1, lst2, diff=0):
        if diff:
            node, carry = _add_lsts(lst1.next_node, lst2, diff - 1)
        else:
            if not lst1 and not lst2:
                return None, 0
            node, carry = _add_lsts(lst1.next_node, lst2.next_node)

        aggregate = lst2.value if not diff else 0
        aggregate += lst1.value + carry

        value, carry = aggregate % 10, aggregate / 10
        new_node = Node(value, node)

        return new_node, carry

    lst1_cur, lst2_cur = lst1, lst2
    while lst1_cur and lst2_cur:
        lst1_cur = lst1_cur.next_node
        lst2_cur = lst2_cur.next_node

    # lst1 is now the longer linked list
    if not lst1_cur:
        lst2, lst1 = lst1, lst2

    diff = 0
    while lst1_cur:
        lst1_cur = lst1_cur.next_node
        diff += 1

    node, carry = _add_lsts(lst1, lst2, diff)
    return Node(carry, node) if carry else node


def solution2(lst1, lst2):
    def prev_mapper(lst, cur_to_pre):
        prev, cur = None, lst
        while cur:
            cur_to_pre[cur] = prev
            prev, cur = cur, cur.next_node
        return prev

    cur_to_pre = {}
    tail1 = prev_mapper(lst1, cur_to_pre)
    tail2 = prev_mapper(lst2, cur_to_pre)

    carry = 0
    node = None
    while carry or tail1 or tail2:
        aggregate = carry
        if tail1: aggregate += tail1.value; tail1 = cur_to_pre[tail1]
        if tail2: aggregate += tail2.value; tail2 = cur_to_pre[tail2]

        value, carry = aggregate % 10, aggregate / 10
        node = Node(value, node)
    return node
