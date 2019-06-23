class Solution:
    def removeElement(self, nums: int(), val: int) -> int:
        if len(nums) == 0:
            return 0
        nums = list.sort(nums)
        i = 0
        for j in range(1, len(nums)):
            

solution = Solution()
solution.removeElement([1,2,3,2,1], 2)