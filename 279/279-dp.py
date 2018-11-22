import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return -1
        
        f = [(1 << 31) - 1 for _ in range(n + 1)]
        f[0] = 0
        
        for i in range(1, n + 1):
            least_num = (1 << 31) - 1
            for j in range(int(math.sqrt(n)) + 1):
                if f[i - j * j] != (1 << 31) - 1:
                    least_num = min(least_num, f[i - j * j] + 1)
                    
            f[i] = least_num
        
        return f[n]
                    
        