from typing import List


class Solution(object):
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        length = len(triangle)
        if length == 1:
            return triangle[0][0]
        for i in range(1, length):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        return min(triangle[-1])
