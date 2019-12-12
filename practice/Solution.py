class Solution(object):
    
    def moveZeros(self, nums: list) -> list:
        if nums is None or len(nums) == 1:
            return nums
        length = len(nums)
        index = 0
        for i in range(0, length):
            if nums[i] != 0:
                nums[index] = nums[i]
                if (i != index):
                    nums[i] = 0
                index = index + 1
        return nums

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        pre = 1
        next = 2
        steps = 0
        for i in range(0, n - 2):
            steps = pre + next
            pre = next
            next = steps
        return steps

    def threeSum(self, nums: list) -> list:
        if nums is None:
            return None
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = list()
        for i in range(0, length):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = length - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif sum < 0:
                    L = L + 1
                else:
                    R = R - 1
        return result

    def maxArea(self, height: list) -> int:
        if height is None:
            return None
        length = len(height)
        if length < 2:
            return 0
        if length < 3:
            return height[0] if height[0] < height[1] else height[1]
        L = 0
        R = length - 1
        max = 0
        while R != L:
            if height[R] >= height[L]:
                area = (R - L) * height[L]
                L = L + 1
            else:
                area = (R - L) * height[R]
                R = R - 1
            max = max if area <= max else area
        return max


if __name__ == "__main__":
    solution = Solution()

    # nums = [1, 0, -1, 5, 0, -5, 7, 0, 6]
    # print(solution.moveZeros(nums))

    # n = 5
    # print(solution.climbStairs(5))

    # print(solution.threeSum(nums))

    height = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))