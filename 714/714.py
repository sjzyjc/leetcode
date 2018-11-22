class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        
        pre_hold = 0
        pre_sell = 0
        for i in range(1, len(prices)):
            sell = max(pre_sell, pre_hold + prices[i] - prices[i - 1] - fee)
            hold = max(pre_sell, pre_hold + prices[i] - prices[i - 1])
            pre_sell = sell
            pre_hold = hold
        
        return sell
                