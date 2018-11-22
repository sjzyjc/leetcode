class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        f = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s) - 1):
            f[i][i] = 1
            
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2
            else:
                f[i][i + 1] = 1
                
        f[-1][-1] = 1
                
        return self.helper(s, 0, len(s) - 1, f)
    
    def helper(self, s, i, j, f):
        if f[i][j] != -1:
            return f[i][j]
        
        if i < 0 or j >= len(s):
            return 0
        
        max_len = 1
        if s[i] == s[j]:
            max_len = self.helper(s, i + 1, j - 1, f) + 2
        else:
            max_len = max(self.helper(s, i, j - 1, f), self.helper(s, i + 1, j, f))
            
        f[i][j] = max_len
        
        return f[i][j]
                
