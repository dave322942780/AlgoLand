# https://careercup.com/question?id=5765433895419904


def solution(intervals):
    def comparator(x, y):
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        else:
            return 0

    intervals = sorted(intervals, comparator)
    non_overlapping_intervals = []
    for interval in intervals:
        if not non_overlapping_intervals or non_overlapping_intervals[-1][1] < interval[0]:
            non_overlapping_intervals.append(interval)
        else:
            non_overlapping_intervals[-1][1] = max(non_overlapping_intervals[-1][1], interval[1])
    duration = 0
    while non_overlapping_intervals:
        dur = non_overlapping_intervals.pop()
        duration += dur[1] - dur[0]
    return duration
