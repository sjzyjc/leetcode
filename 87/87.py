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
        
        f = [[[False for _ in range(len(s1) + 1)] for _ in range(len(s1))] for _ in range(len(s1))]
        
        for i in range(len(s1)):
            for j in range(len(s1)):
                f[i][j][1] = (s1[i] == s2[j])
            
        for l in range(2, len(s1) + 1):
            for i in range(len(s1) - l + 1):
                for j in range(len(s1) - l + 1):
                    for k in range(1, l):
                        if f[i][j][l]:
                            break
                        f[i][j][l] = (f[i][j][k] and f[i + k][j + k][l - k]) or (f[i][j + l - k][k] and f[i + k][j][l - k])
        
        
        return f[0][0][len(s1)]
                        
        