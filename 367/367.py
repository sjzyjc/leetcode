class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        start, end = 1, num - 1
        while start <= end:
            mid = start + (end - start) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1                
            else:
                end = mid - 1
                
        return False
                
        