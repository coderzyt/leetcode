class Solution(object):
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        if n < 3:
            return n
        steps, step1, step2 = 0, 1, 2
        for i in range(3, n + 1):
            steps = step1 + step2
            step1 = step2
            step2 = steps
        return steps



if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))