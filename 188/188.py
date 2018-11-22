class Solution:
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        if k > len(prices) // 2:
            ans = 0
            for index, price in enumerate(prices):
                if index > 0 and price > prices[index - 1]:
                    ans += price - prices[index - 1]
                    
            return ans
        
        int_min = - (1 << 31)
        f = [[int_min for i in range(2*k + 1)] for j in range(len(prices) + 1)]
        f[0][0] = 0
        
        for i in range(1, len(prices) + 1):
            #no stock at hand
            for state in range(0, 2*k + 1, 2):
                if i - 2 < 0 or state - 1 < 0 or f[i -1][state - 1] == int_min:
                    f[i][state] = f[i - 1][state]
                    continue
                    
                profit = max(f[i - 1][state], f[i - 1][state - 1] + prices[i - 1] - prices[i - 2])
                f[i][state] = profit
                
            for state in range(1, 2*k, 2):
                if i - 2 < 0 or f[i - 1][state] == int_min:
                    f[i][state] = f[i - 1][state - 1]
                    continue
                    
                profit = max(f[i - 1][state] + prices[i - 1] - prices[i - 2], f[i - 1][state - 1])
                f[i][state] = profit
        
        ans = - (1 << 31)
        for i in range(0, 2*k + 1, 2):
            ans = max(ans, f[-1][i])
            
        return ans