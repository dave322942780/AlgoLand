# https://www.careercup.com/question?id=22809662

def solution(lst):
    height = [-1, ] * len(lst)
    max_height = 0

    def update_height(idx):
        if height[idx] > 0:
            return
        elif lst[idx] == -1:
            height[idx] = 0
        else:
            update_height(lst[idx])
            height[idx] = height[lst[idx]] + 1

    for i in range(len(lst)):
        update_height(i)
        max_height = max(max_height, height[i])
    return max_height
