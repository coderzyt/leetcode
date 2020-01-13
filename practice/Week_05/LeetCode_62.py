class Solution(object):

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for i in range(0, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]

if __name__ == "__main__":
    m = 3
    n = 2
    solution = Solution()
    print(solution.uniquePaths(3, 2))