# http://www.careercup.com/question?id=16759664
from data_structures_basic.IndexedMinQueue import IndexedMinQueue


def solution(lsts):
    min_queue = IndexedMinQueue()
    greedy_iter = []

    for i in range(len(lsts)):
        min_queue.enqueue((i, 0), lsts[i][0])
        greedy_iter.append(lsts[i][0])

    optimal_range = (min(greedy_iter), max(greedy_iter))

    cur = "place_holder"
    while cur:
        cur = min_queue.dequeue()

        if cur:
            greedy_iter[cur[0]] = lsts[cur[0]][cur[1]]
            upper_bound = max(greedy_iter)
            lower_bound = min(greedy_iter)
            if upper_bound - lower_bound <= optimal_range[1] - optimal_range[0]:
                optimal_range = (lower_bound, upper_bound)

        if not cur or cur[1] + 1 >= len(lsts[cur[0]]):
            continue

        min_queue.enqueue((cur[0], cur[1] + 1), lsts[cur[0]][cur[1] + 1])

    return optimal_range
