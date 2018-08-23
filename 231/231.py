class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n > 0:
            if n % 2 == 1 and n != 1:
                return False
            n = n // 2
        return True   