# http://www.careercup.com/question?id=16759664
# difficulty: 4
# length: 5

from Queue import PriorityQueue


def solution(lsts):
    class MinQueue(object):
        class ItemIndexPair(object):
            def __init__(self, key, value):
                self.value = value
                self.index = key

            def __cmp__(self, other):
                return self.value > other.value

        queue = PriorityQueue()

        def enqueue(self, value, index):
            self.queue.put(self.ItemIndexPair(value, index))

        def dequeue(self):
            return self.queue.get().index

    min_queue = MinQueue()

    for i in range(len(lsts)):
        min_queue.enqueue((i, 0), lsts[i][0])

    while True:
        cur = min_queue.dequeue()
        print lsts[cur[0]][cur[1]]
        if cur[1] + 1 >= len(lsts[cur[0]]):
            break
        min_queue.enqueue((cur[0], cur[1] + 1), lsts[cur[0]][cur[1] + 1])
