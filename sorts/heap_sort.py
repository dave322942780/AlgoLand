
def heap_sort(lst):
    end = (len(lst) - 1) / 2 - 1
    for i in range(end, -1, -1):
        left_idx = 2 ** i + 1
        right_idx = 2 ** i + 2


lst = [5, 8, 45, 651, 561, 213, 21]
exp = [5, 8, 21, 45, 213, 561, 651]
assert heap_sort(lst) == exp
assert lst == exp