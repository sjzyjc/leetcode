class Solution:
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        T(N*K)
        O(K)
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
        f = [[int_min for i in range(2*k + 1)] for j in range(2)]
        f[0][0] = 0
        pre, cur = 0, 1
        
        for i in range(1, len(prices) + 1):
            #no stock at hand
            for state in range(0, 2*k + 1, 2):
                if i - 2 < 0 or state - 1 < 0 or f[pre][state - 1] == int_min:
                    f[cur][state] = f[pre][state]
                    continue
                    
                profit = max(f[pre][state], f[pre][state - 1] + prices[i - 1] - prices[i - 2])
                f[cur][state] = profit
                
            for state in range(1, 2*k, 2):
                if i - 2 < 0 or f[pre][state] == int_min:
                    f[cur][state] = f[pre][state - 1]
                    continue
                    
                profit = max(f[pre][state] + prices[i - 1] - prices[i - 2], f[pre][state - 1])
                f[cur][state] = profit
                
            pre, cur = cur, pre
        
        ans = - (1 << 31)
        for i in range(0, 2*k + 1, 2):
            ans = max(ans, f[pre][i])
            
        return ans