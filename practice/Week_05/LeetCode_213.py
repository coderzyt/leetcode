from typing import List


class Solution(object):

    def rob(self, nums: List[int]) -> int:

        def myrob(nums: List[int]) -> int:
            preMax = 0
            curMax = 0
            for i in range(len(nums)):
                curMax, preMax = max(preMax + nums[i], curMax), curMax
            return curMax

        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        return max(myrob(nums[1:]), myrob(nums[:length - 1]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1,2,3,1]))






