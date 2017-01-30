# https://www.careercup.com/question?id=388863

def solution(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next_node
        cur.next_node = prev
        prev = cur
        cur = tmp
    return prev
