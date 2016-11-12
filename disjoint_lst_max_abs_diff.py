# https://careercup.com/question?id=19286747

def solution(lst):
    left_min_ending_here = [None, ] * len(lst)
    left_max_ending_here = [None, ] * len(lst)

    left_min_ending_here[0] = min(lst[0], 0)
    left_min_so_far = min(lst[0], 0)
    left_max_ending_here[0] = max(lst[0], 0)
    left_max_so_far = max(lst[0], 0)

    for i in range(1, len(lst)):
        left_min_so_far = min(left_min_so_far + lst[i], 0)
        left_min_ending_here[i] = min(left_min_so_far, min(left_min_ending_here[:i]))
        left_max_so_far = max(left_max_so_far + lst[i], 0)
        left_max_ending_here[i] = max(left_max_so_far, max(left_max_ending_here[:i]))

    right_min_ending_here = [None, ] * len(lst)
    right_max_ending_here = [None, ] * len(lst)

    right_min_ending_here[-1] = min(lst[-1], 0)
    right_min_so_far = min(lst[-1], 0)
    right_max_ending_here[-1] = max(lst[-1], 0)
    right_max_so_far = max(lst[-1], 0)

    def iabs(x):
        return x if x >= 0 else -1 * x

    for i in range(len(lst) - 2, -1, -1):
        right_min_so_far = min(right_min_so_far + lst[i], 0)
        right_min_ending_here[i] = min(right_min_so_far, min(right_min_ending_here[i + 1:]))
        right_max_so_far = max(right_max_so_far + lst[i], 0)
        right_max_ending_here[i] = max(right_max_so_far, max(right_max_ending_here[i + 1:]))

    max_abs_sum = 0
    max_abs_sum_idx = 0
    left_abs_max_lst = None
    right_abs_max_lst = None

    def iabs(x):
        return x if x >= 0 else -1 * x

    for i in range(len(lst) - 1):
        left_max = max(iabs(left_max_ending_here[i]), iabs(left_min_ending_here[i]))
        right_max = max(iabs(right_max_ending_here[i + 1]), iabs(right_min_ending_here[i + 1]))
        if left_max + right_max > max_abs_sum:
            max_abs_sum = left_max + right_max
            max_abs_sum_idx = i
            left_abs_max_lst = left_max_ending_here if iabs(left_max_ending_here[i]) == left_max \
                else left_min_ending_here
            right_abs_max_lst = right_max_ending_here if iabs(right_max_ending_here[i + 1]) == right_max \
                else right_min_ending_here
    i = max_abs_sum_idx
    left_prev_val = left_abs_max_lst[i]
    j = max_abs_sum_idx + 1
    right_prev_val = right_abs_max_lst[j]

    while i >= 0 and left_prev_val == left_abs_max_lst[i - 1]:
        i -= 1

    while j < len(lst) - 1 and right_prev_val == right_abs_max_lst[j + 1]:
        j += 1

    left_res_end = i + 1
    right_res_start = j

    while i >= 0 and lst[i] != left_abs_max_lst[i]:
        i -= 1

    while j < len(lst) - 1 and lst[j] != right_abs_max_lst[j]:
        j += 1

    left_res_start = i
    right_res_end = j + 1

    return [lst[left_res_start:left_res_end], lst[right_res_start:right_res_end], max_abs_sum]
