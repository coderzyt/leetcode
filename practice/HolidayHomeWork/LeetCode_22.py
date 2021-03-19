from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate(curString: str, result: list, left: int, right: int, n: int) -> list:
            if len(curString) == 2 * n:
                result.append(curString)
                return
            if left < n:
                _generate(curString + '(', result, left + 1, right, n)
            if right < left:
                _generate(curString + ')', result, left, right + 1, n)
        if n <= 0:
            return []
        result, left, right = [], 0, 0
        _generate('', result, left, right, n)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
