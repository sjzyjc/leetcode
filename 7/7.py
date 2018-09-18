class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        
        ans = 0
        while x > 0:
            ans = ans * 10 + (x % 10)
            x = x // 10
            
        
        if is_negative:
            ans = - ans
            
        if ans > (1 << 31) - 1 or ans < - (1 << 31):
            return 0
        
        return ans