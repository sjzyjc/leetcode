class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * current_product
                
            current_product *= current_product
            n = n >> 1
        
        return ans