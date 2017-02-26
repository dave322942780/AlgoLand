# https://www.careercup.com/question?id=5739192933941248


def solution(peoples_availabilities):
    def build_heap():
        heap = filter(lambda x: bool(x), peoples_availabilities[:])
        for i in range(len(heap) - 1, -1, -1):
            j = i
            do_break = False
            while j > 0 and not do_break:
                parent = (j - 1) / 2
                if heap[parent][0][0] > heap[j][0][0]:
                    heap[j], heap[parent] = heap[parent], heap[j]
                    j = parent
                else:
                    do_break = True
        return heap

    def get_min(heap, heap_tracker):
        def heap_by_idx(heap_idx):
            heap_tracker.setdefault(id(heap[heap_idx]), 0)
            return heap[heap_idx][heap_tracker[id(heap[heap_idx])]]

        if not heap:
            return None
        min_lst = heap[0]
        heap_tracker.setdefault(id(min_lst), 0)
        min_item = min_lst[heap_tracker[id(min_lst)]]
        heap_tracker[id(min_lst)] += 1
        if heap_tracker[id(min_lst)] >= len(min_lst):
            if len(heap) > 1:
                heap[0] = heap.pop()
            else:
                return None
        cur = 0
        while True:
            pre_cur = cur
            left = cur * 2 + 1
            right = cur * 2 + 2
            if right < len(heap):
                if heap_by_idx(cur)[0] > heap_by_idx(left)[0] and heap_by_idx(right)[0] > heap_by_idx(left)[0]:
                    heap[cur], heap[left] = heap[left], heap[cur]
                    cur = left
                elif heap_by_idx(cur)[0] > heap_by_idx(right)[0]:
                    heap[cur], heap[right] = heap[right], heap[cur]
                    cur = right
            elif left < len(heap):
                if heap_by_idx(cur)[0] > heap_by_idx(left)[0]:
                    heap[cur], heap[left] = heap[left], heap[cur]
            if pre_cur == cur:
                break
        return min_item

    heap_tracker = {}
    heap = build_heap()
    latest_finish_time = None
    res = []
    while True:
        cur = get_min(heap, heap_tracker)
        if cur is None:
            break
        if latest_finish_time:
            if latest_finish_time < cur[0]:
                if res and res[-1][0] == latest_finish_time:
                    res.pop()
                res.append((latest_finish_time, cur[0]))
            latest_finish_time = max(latest_finish_time, cur[1])
        else:
            latest_finish_time = cur[1]
    return res
