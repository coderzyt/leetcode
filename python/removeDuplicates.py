class Solution:
    def removeDuplicates(self, nums: int()) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1


li = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
solution.removeDuplicates(li)
