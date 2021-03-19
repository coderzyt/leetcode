class Solution(object):
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.fib(n, memo)

    def fib(self, i: int, memo: []) -> int:
        if i < 3:
            memo[i] = i
        if memo[i] == 0:
            memo[i] = self.fib(i - 1, memo) + self.fib(i - 2, memo)
        return memo[i]



if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(2))