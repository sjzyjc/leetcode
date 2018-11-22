class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        pre_buy_price = prices[0]
        
        for price in prices:
            if price > pre_buy_price:
                max_profit += (price - pre_buy_price)
            
            pre_buy_price = price
            
        return max_profit
                
            