def solution(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next_node
        cur.next_node = prev
        prev = cur
        cur = tmp
    return prev
