from typing import List


class Solution(object):

    def search(self, nums: List[int]) -> int:
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return mid
            elif nums[right] < nums[mid]:
                left = mid
            else:
                right = mid
        return None


if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,8,0,1,2,3]
    print(solution.search(nums))
