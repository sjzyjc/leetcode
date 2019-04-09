class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0: 
            return False
        
        orig_x = x
        reverse = 0
        while x > 0:  
            reverse = reverse * 10 + x % 10
            x //= 10
            
        return orig_x == reverse