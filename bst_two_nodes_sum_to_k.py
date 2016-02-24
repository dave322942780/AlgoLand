# http://www.careercup.com/question?id=15320677
# Given a BST and a value x. Find two nodes in the tree whose sum is equal x.
# Additional space: O(height of the tree). It is not allowed to modify the tree

from data_structures_basic.BSTQueue import MinBSTQueue, MaxBSTQueue


def solution(root, k):
    min_bst_queue = MinBSTQueue(root)
    max_bst_queue = MaxBSTQueue(root)
    i = min_bst_queue.get()
    j = max_bst_queue.get()
    while i is not j:
        i_j_sum = i.value + j.value
        if i_j_sum == k:
            return i, j
        elif i_j_sum > k:
            j = max_bst_queue.get()
        elif i_j_sum < k:
            i = min_bst_queue.get()
    return None
