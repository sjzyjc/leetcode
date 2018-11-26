class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None and t is None:
            return 1
        
        if len(s) == 0 and len(t) == 0:
            return 1
        
        if (not s) != (not t):
            return 0
        
        f = [0 for _ in range(len(t) + 1)]
        f[0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(len(t), 0, -1):
                if s[i - 1] == t[j - 1]:
                    f[j] += f[j - 1]
        
        return f[-1]