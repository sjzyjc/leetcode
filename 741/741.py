class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
    
        hold = -max(prices)
        sell = 0
        for i in range(len(prices)):
            sell = max(sell, hold + prices[i] - fee)
            hold = max(hold, sell - prices[i])
        
        return sell
                