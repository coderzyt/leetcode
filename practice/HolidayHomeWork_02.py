from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        length = len(nums)
        nums.sort()
        result = []
        for i in range(0, length):
            if nums[i] > 0:
                return result
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            a, b = i + 1, length - 1
            while a < b:
                if nums[a] + nums[b] > -nums[i]:
                    b = b - 1
                elif nums[a] + nums[b] < -nums[i]:
                    a = a + 1
                else:
                    result.append([nums[i], nums[a], nums[b]])
                    while a < b and nums[a] == nums[a + 1]:
                        a = a + 1
                    while a < b and nums[b] == nums[b - 1]:
                        b = b - 1
                    a = a + 1
                    b = b - 1
        return result



if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
