class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]

        for i in range(1,n):
            if prices[i] < min_price:
                min_price = prices[i]

            if (prices[i] - min_price) > max_profit:
                max_profit = (prices[i] - min_price)

        return max_profit    
            



           
            
