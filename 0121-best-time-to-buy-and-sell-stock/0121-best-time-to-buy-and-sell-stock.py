class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float("inf")

        for i in range(n):
            min_price = min(min_price, prices[i])
            diff = prices[i] - min_price
            max_profit = max(max_profit, diff)
        return max_profit

        