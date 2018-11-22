class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        O(N)
        O(1)
        """
        if not prices:
            return 0
        
        min_buy = prices[0]
        max_profit = 0
        
        for price in prices:
            if price - min_buy > max_profit:
                max_profit = price - min_buy
                
            if price < min_buy:
                min_buy = price
                
        return max_profit
        