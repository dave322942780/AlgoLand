# https://leetcode.com/problems/jump-game-ii/description/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        step_number = 0

        cur_max = nums[0]
        to_visit = (1, 1 + cur_max)

        while True:
            new_max = to_visit[1]
            step_number += 1
            if new_max >= len(nums):
                return step_number
            for i in range(to_visit[0], to_visit[1]):
                new_max = max(new_max, nums[i] + i + 1)
            to_visit = (to_visit[1], new_max)



