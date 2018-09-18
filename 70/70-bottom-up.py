class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        f = {}
        f[0] = 1
        for i in range(1, n + 1):
            f[i] = 0
            if i >= 1:
                f[i] += f[i - 1]
            
            if i >=2:
                f[i] += f[i - 2]
                
        return f[n]
            