from typing import List


class Solution(object):
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        res = [[0] * 2 for _ in range(length)]
        for i in range(len(nums)):
            res[i][0] = res[i - 1][1]
            res[i][1] = res[i - 1][0] + nums[i]
        return max(res[length - 1][0], res[length - 1][1])

    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        res = [0] * length
        for i in range(length):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])
        return res[length - 1]




if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2,7,9,3,1]))
