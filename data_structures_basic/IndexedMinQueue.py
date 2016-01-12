from Queue import PriorityQueue


class IndexedMinQueue(object):
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
        if self.queue.empty():
            return None
        return self.queue.get().index
