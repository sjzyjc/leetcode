class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1 is None) != (s2 is None):
            return False
        
        if s1 is None and s2 is None:
            return True
        
        if len(s1) != len(s2):
            return False
        
        f = [[[-1 for _ in range(len(s1) + 1)] for _ in range(len(s1))] for _ in range(len(s1))]
        
        for i in range(len(s1)):
            for j in range(len(s1)):
                f[i][j][1] = (s1[i] == s2[j])
            
        return self.helper(0, 0, len(s1), f)
        
    def helper(self, i, j, l, f):
        if f[i][j][l] != -1:
            return f[i][j][l]
            
        tmp = False
        for k in range(1, l):
            if not tmp:
                tmp = self.helper(i, j ,k, f) and self.helper(i + k, j + k, l - k, f)
            
            if not tmp:
                tmp = self.helper(i, j + l - k, k, f) and self.helper(i + k, j, l - k, f)
                
        
        f[i][j][l] = tmp
        return f[i][j][l]
            
            
        
                        
        