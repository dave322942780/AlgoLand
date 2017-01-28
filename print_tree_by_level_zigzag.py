def solution(root):
    cur_stack = [root]
    backup_stack = []
    l_to_r = True
    res = []
    while cur_stack or backup_stack:
        if cur_stack:
            node = cur_stack.pop()
            res.append(node.value)
            if l_to_r:
                if node.right: backup_stack.append(node.right)
                if node.left: backup_stack.append(node.left)
            else:
                if node.left: backup_stack.append(node.left)
                if node.right: backup_stack.append(node.right)

        else:
            cur_stack = backup_stack
            backup_stack = []
            l_to_r = not l_to_r
    return "".join(map(lambda x: str(x), res))

