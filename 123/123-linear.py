class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        h1 = h2 = -max(prices)
        s1 = s2 = 0
        for price in prices:
            h1 = max(h1, -price)
            s1 = max(s1, h1 + price)
            h2 = max(h2, s1 - price)
            s2 = max(s2, h2 + price)
            
        return s2
        