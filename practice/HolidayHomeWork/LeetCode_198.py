from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        last, cur = 0, 0
        for i in range(len(nums)):
            last, cur = cur, max(last + nums[i], cur)
        return cur


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2]
    print(solution.rob(nums))
