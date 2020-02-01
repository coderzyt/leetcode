from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def helper(string: str, digitsLeft: str):
            if not digitsLeft:
                result.append(string)
            else:
                for letter in hashMap[digitsLeft[0]]:
                    helper(string + letter, digitsLeft[1:])

        result = []
        if digits:
            helper('', digits)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))