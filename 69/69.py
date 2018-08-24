class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid - 1
        
        if end * end > x:
            return start
        else: 
            return end