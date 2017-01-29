# https://careercup.com/question?id=16230693

def solution(nums, target):
    size = len(nums)
    ops = [[]]
    for i in range(size):
        new_ops = []
        for op in ops:
            for i in (1, 0, -1):
                new_ops.append(op + [i])
        ops = new_ops
    ops.pop()

    res = []
    for op in ops:
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += op[i] * nums[i]
        if cur_sum == target:
            res.append(op)
    return res
