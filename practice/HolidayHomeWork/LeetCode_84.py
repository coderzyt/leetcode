from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        maxArea = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                maxArea = max(maxArea, heights[index] * (i - stack[-1] - 1))
            stack.append(i)
        return maxArea
            

        stack = []
        # 单调递增栈
        maxmun = 0
        heights = [0] + heights + [0]    # 添加左右两侧的特殊边界使得只有一个柱子时，也可以形成一个倒V型
        
        for i in range(len(heights)):
            # 对于stack[-1]来说其right_i=i，left_i=stack[-2]
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                s = (i - stack[-1] - 1) * heights[top]
                maxmun = max(s, maxmun)

            stack.append(i)

        return maxmu
        