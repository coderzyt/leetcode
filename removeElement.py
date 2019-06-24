class Solution:
    def removeElement(self, nums: int(), val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i

solution = Solution()
solution.removeElement([3,3,4,4,3, 4, 5], 3)