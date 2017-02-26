# https://www.careercup.com/question?id=5689208527126528


def solution(tree):
    def get_longest_consecutive(node):
        if node:
            if not node.left and not node.right:
                return node, True, 0, 0, 0
            else:
                l_longest, l_is_left, l_len, l_l, l_r = get_longest_consecutive(node.left)
                r_longest, r_is_left, r_len, r_l, r_r = get_longest_consecutive(node.right)
                max_length = max(max(l_l, r_r) + 1, l_len, r_len)

                if max_length == l_len:
                    return l_longest, l_is_left, l_len, l_l + 1, r_r + 1
                elif max_length == r_len:
                    return r_longest, r_is_left, r_len, l_l + 1, r_r + 1
                elif max_length == l_l + 1:
                    return node, True, l_l + 1, l_l + 1, r_r + 1
                elif max_length == r_r + 1:
                    return node, False, r_r + 1, l_l + 1, r_r + 1
        else:
            return None, None, -1, -1, -1

    return get_longest_consecutive(tree)[:2]
