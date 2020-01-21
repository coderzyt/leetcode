class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = [-1]
        length = len(s)
        maxLength = 0
        for i in range(length):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i - stack[-1])
        return maxLength