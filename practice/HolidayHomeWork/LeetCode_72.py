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
        if length1 == length2:
            



if __name__ == "__main__":
    pass