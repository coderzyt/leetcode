from typing import List


class Solution(object):
    
    def myPow(self, x: float, n: int) -> float:
        result = x
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n > 0:
            for i in range(0, n - 1):
                result = result * x
            return result
        else:
            for i in range(0, n):
                result = result * x
            return 1 / result

    def subsets(self, nums: List[List[int]]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            newsets = []
            for subset in result:
                new_subset = subset + [num]
                newsets.append(new_subset)
            result.extend(newsets)
        return result

if __name__ == "__main__":
    solution = Solution()
    # print(solution.myPow(2, 10))

    print(solution.subsets([1, 2, 3]))