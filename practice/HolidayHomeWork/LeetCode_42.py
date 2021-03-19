from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        left, right = 0, length - 1
        leftMax = height[0]
        rightMax = height[length - 1]
        maxArea = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                maxArea += leftMax - height[left]
                left += 1
            else:
                maxArea += rightMax - height[right]
                right -= 1
        return maxArea