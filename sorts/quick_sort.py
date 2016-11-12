def _quick_sort(lst, start, end):
    if end - start <= 1:
        return
    else:
        pivot = lst[start]
        left_cur_idx = start + 1
        right_cur_idx = end - 1
        finish = False

        while not finish:
            while left_cur_idx <= right_cur_idx and lst[left_cur_idx] <= pivot:
                left_cur_idx += 1
            while left_cur_idx <= right_cur_idx and lst[right_cur_idx] >= pivot:
                right_cur_idx -= 1
            if left_cur_idx < right_cur_idx:
                lst[left_cur_idx], lst[right_cur_idx] = lst[right_cur_idx], lst[left_cur_idx]
            else:
                finish = True

        lst[start], lst[right_cur_idx] = lst[right_cur_idx], lst[start]
        _quick_sort(lst, start, right_cur_idx)
        _quick_sort(lst, right_cur_idx + 1, end)


def quick_sort(lst):
    _quick_sort(lst, 0, len(lst))
    return lst


lst = [5, 8, 45, 651, 561, 213, 21, 1000]
exp = [5, 8, 21, 45, 213, 561, 651, 1000]
assert quick_sort(lst) == exp
assert lst == exp
