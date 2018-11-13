class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num or num <= 0:
            return False
        
        while num > 1 and num % 2 == 0:
            num /= 2
            
        while num > 1 and num % 3 == 0:
            num /= 3
            
        while num > 1 and num % 5 == 0:
            num /= 5
        
        return num == 1
