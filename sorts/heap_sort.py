
def heap_sort(lst):
    for i in range(len(lst)):
        cur = i
        parent = (i - 1) / 2
        while parent >= 0:
            if lst[parent] < lst[cur]:
                lst[parent], lst[cur] = lst[cur], lst[parent]
            else:
                break
            cur = parent
            parent = (parent - 1) / 2
    j = len(lst) - 1
    while j != 0:
        lst[0], lst[j] = lst[j], lst[0]
        cur = 0
        left = 2 * cur + 1
        right = 2 * cur + 2
        # if there's at least a left child
        while left < j:
            # if there's a right child / 2 children
            if right < j:
                max_cmp = max(lst[cur], lst[left], lst[right])
                if max_cmp == lst[cur]:
                    break
                elif max_cmp == lst[left]:
                    lst[cur], lst[left] = lst[left], lst[cur]
                    cur = left
                else:
                    lst[cur], lst[right] = lst[right], lst[cur]
                    cur = right
            # if there's only left child
            else:
                if lst[left] > lst[cur]:
                    lst[cur], lst[left] = lst[left], lst[cur]
                    cur = left
                else:
                    break
            left = 2 * cur + 1
            right = 2 * cur + 2
        j -= 1
    return lst


lst = [5, 8, 45, 651, 561, 213, 21]
exp = [5, 8, 21, 45, 213, 561, 651]
assert heap_sort(lst) == exp
# assert lst == exp