class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        O(N)
        O(N)
        """
        if not prices:
            return 0
        
        int_min = - (1 << 31)
        f = [[int_min for i in range(5)] for j in range(len(prices) + 1)]
        f[0][0] = 0
        
        for i in range(1, len(prices) + 1):
            #no stock at hand
            for state in [0, 2, 4]:
                if i - 2 < 0 or state - 1 < 0 or f[i -1][state - 1] == int_min:
                    f[i][state] = f[i - 1][state]
                    continue
                    
                profit = max(f[i - 1][state], f[i - 1][state - 1] + prices[i - 1] - prices[i - 2])
                f[i][state] = profit
                
            for state in [1, 3]:
                if i - 2 < 0 or f[i - 1][state] == int_min:
                    f[i][state] = f[i - 1][state - 1]
                    continue
                    
                profit = max(f[i - 1][state] + prices[i - 1] - prices[i - 2], f[i - 1][state - 1])
                f[i][state] = profit
        
        return max(f[-1][0], f[-1][2], f[-1][4])