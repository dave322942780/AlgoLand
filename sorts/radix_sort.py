def radix_sort(lst):
    terminate = False
    digit = 0
    base = 2

    while not terminate:
        buckets = [[] for i in range(base)]
        terminate = True
        for num in lst:
            num_at_digit = num / (base ** digit) % base
            terminate &= num / (base ** digit) == 0
            buckets[num_at_digit].append(num)
        while lst:
            lst.pop()
        for bucket in buckets:
            for i in bucket:
                lst.append(i)
        digit += 1
    return lst


lst = [5, 8, 45, 651, 561, 213, 21]
exp = [5, 8, 21, 45, 213, 561, 651]
assert radix_sort(lst) == exp
assert lst == exp
