from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, leftDiagonal, rightDiagonal):
            row = len(queens)
            if row >= n:
                result.append(queens)
            else:
                for col in range(n):
                    if col not in queens and row + col not in leftDiagonal and col - row not in rightDiagonal:
                        DFS(queens + [col], leftDiagonal + [row + col], rightDiagonal + [col - row])
        result = []
        DFS([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))