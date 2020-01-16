from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = [[0] * 2 for _ in range(len(prices))]
        for i in range(len(prices)):
            if i == 0:
                profit[i][0] = 0
                profit[i][1] = -prices[i]
                continue
            profit[i][0] = max(profit[i - 1][1] + prices[i], profit[i - 1][0])
            profit[i][1] = max(profit[i - 1][1], -prices[i])
        return profit[len(prices) - 1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit_i_0, profit_i_1 = 0, 0
        for i in range(len(prices)):
            profit_i_0 = max(profit_i_0, profit_i_1 + prices[i])
            profit_i_1 = max(profit_i_1, -prices[i])
        return profit_i_0


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))