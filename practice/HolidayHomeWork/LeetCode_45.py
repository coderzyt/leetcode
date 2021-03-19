from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        maxLength = 0
        for i in range(len(nums)-1):
            maxLength = max(maxLength, nums[i]+i)
            if(i == end):
                step += 1
                end = maxLength
        return step
