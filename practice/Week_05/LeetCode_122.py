from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit_i_0, profit_i_1 = 0, 0
        for i in range(len(prices)):
            temp = profit_i_0
            profit_i_0 = max(profit_i_0, profit_i_1 + prices[i])
            profit_i_1 = max(profit_i_1, temp - prices[i])
        return profit_i_0

