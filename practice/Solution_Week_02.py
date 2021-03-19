from typing import List


class Solution(object):

    def generateParenthesis(self, n: int) -> List[str]:
        result = List[int]
        left = 0
        right = 0
        self.generate(left, right, n, "", result)
        return result

    def generate(self, left: int, right: int, n: int, currentStr: str, result: List[int]):
        if left + right >= 2 * n:
            print(currentStr)
            return

        s1 = currentStr + "{"
        s2 = currentStr + "}"

        left += 1
        right += 1

        self.generate(left, right, n, s1, result)
        self.generate(left, right, n, s2, result)



    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return n
        step1 = 1
        step2 = 2
        steps = 0
        for i in range(0, n - 2):
            steps = step1 + step2
            step1 = step2
            step2 = steps
        return steps

if __name__ == '__main__':
    solution = Solution()
    # print(solution.climbStairs(4))

    solution.generateParenthesis(3)