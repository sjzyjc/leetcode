class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        f = [[0 for j in range(2)] for i in range(len(prices) + 1)]
        #0 for not hold, 1 for holding stock
        
        for i in range(1, len(prices) + 1):
            #not hold stock
            f[i][0] = f[i - 1][0]
            if i >= 2:
                f[i][0] = max(f[i][0], f[i - 1][1] + prices[i - 1] - prices[i - 2])
            
            #hold stock
            if i >= 2:
                f[i][1] = max(f[i - 1][1] + prices[i - 1] - prices[i - 2], f[i - 2][0])
                
        return f[-1][0]
            
        