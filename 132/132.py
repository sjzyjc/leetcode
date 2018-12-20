class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        n^2
        n^2
        """
        if not s:
            return 0
        
        is_palin = self.calPlin(s)
        
        f = [0 for i in range(len(s) + 1)]
        f[0] = 0
        
        for i in range(1, len(s) + 1):
            min_palin = (1 << 31) - 1
            for j in range(i):
                if is_palin[j][i - 1]:
                    min_palin = min(min_palin, f[j] + 1)
                    
            f[i] = min_palin
            
        return f[-1] - 1
    
    def calPlin(self, s):
        f = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for mid in range(len(s)):
            i = j = mid
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                f[i][j] = True
                i -= 1
                j += 1
                
            i = mid
            j = mid + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                f[i][j] = True
                i -= 1
                j += 1
                
        return f    
    