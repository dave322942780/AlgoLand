def solution(stack):
    secondary_stack = []
    for i in range(len(stack), 0, -1):
        min_elem = stack.pop()
        for j in range(i - 1):
            cur = stack.pop()
            if min_elem < cur:
                cur, min_elem = min_elem, cur
            secondary_stack.append(cur)
        while stack:
            secondary_stack.append(stack.pop())
        secondary_stack.append(min_elem)
        while secondary_stack:
            stack.append(secondary_stack.pop())
    return stack
