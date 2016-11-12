def _merge_sort(lst, start, end):
    if end - start <= 1:
        return
    else:
        mid = ((end - start) / 2) + start
        _merge_sort(lst, start, mid)
        _merge_sort(lst, mid, end)
        i = start
        j = mid
        sub_lst = []
        while i < mid and j < end:
            if lst[i] < lst[j]:
                sub_lst.append(lst[i])
                i += 1
            else:
                sub_lst.append(lst[j])
                j += 1
        sub_lst.extend(lst[i:mid])
        sub_lst.extend(lst[j:end])
        for i in range(start, end):
            lst[i] = sub_lst[i - start]


def merge_sort(lst):
    _merge_sort(lst, 0, len(lst))
    return lst


lst = [5, 8, 45, 651, 561, 213, 21]
exp = [5, 8, 21, 45, 213, 561, 651]
assert merge_sort(lst) == exp
assert lst == exp
