class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        minus = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            minus = True
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ret = 0
        for shift in range(31, -1, -1):
            if divisor << shift > dividend:
                continue
               
            dividend -= divisor << shift
            ret += (1 << shift)  
            
        if minus:
            ret = -ret
        
        if ret > (1 << 31) - 1 or ret < - (1 << 31):
            return (1 << 31) - 1
        
        return ret
