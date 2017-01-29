# https://careercup.com/question?id=12986664

def solution(lst):
    i = 0
    prev_zeros = 0
    while i < len(lst):

        if prev_zeros and lst[i]:
            rep_idx = i - prev_zeros
            lst[i], lst[rep_idx] = lst[rep_idx], lst[i]
            prev_zeros -= 1

        if lst[i] == 0:
            prev_zeros += 1
        else:
            prev_zeros = 0

        i += 1
    return lst
