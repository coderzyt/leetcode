from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        res = 0
        max_num = nums[0]
        min_num = nums[0]
        for i in range(1, length):
            if nums[i] < 0:
                max_num, min_num = min_num, max_num
            max_num = max(max_num * nums[i], nums[i])
            min_num = min(min_num * nums[i], nums[i])
            res = max(max_num, res)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-2,0,-1,1]))