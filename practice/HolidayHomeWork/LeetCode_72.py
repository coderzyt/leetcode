class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and word2:
            return len(word2)
        if not word2 and word1:
            return len(word1)
        if not word1 and not word2:
            return 0
        length1 = len(word1)
        length2 = len(word2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, length2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            inserted = 1 + self.minDistance(word1, word2[1:])
            deleted = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            return min(inserted, deleted, replace)
            

if __name__ == "__main__":
    pass