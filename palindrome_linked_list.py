# https://careercup.com/question?id=5072809853190144


def solution(l_lst):
    def _solution(left=l_lst, right=l_lst):
        # if fast runner did not reached end
        if right.next_node and right.next_node.next_node:
            is_palindrome, cur_node = _solution(left.next_node, right.next_node.next_node)
            return (is_palindrome and left.value == cur_node.value), cur_node.next_node
        # if fast runner reached end, and lst is even length
        elif right.next_node:
            return (left.value == left.next_node.value), left.next_node.next_node
        # if fast runner reached end, and lst is odd length
        else:
            return True, left.next_node

    return _solution(l_lst, l_lst)[0]
