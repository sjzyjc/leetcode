class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_price = -max(prices)
        hold = [max_price for _ in range(len(prices))]
        sell = [0 for _ in range(len(prices))]
        
        for index, price in enumerate(prices):
            if index > 0:
                sell[index] = max(sell[index - 1], hold[index - 1] + price)
            
            if index > 1:
                hold[index] = max(hold[index - 1], sell[index - 2] - price)
            else:
                hold[index] = max(hold[index - 1], -price)
                
        return max(sell)
            
        