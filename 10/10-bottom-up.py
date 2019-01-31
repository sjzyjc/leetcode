class Solution(object):
    def isMatch(self, s, p):
        # time: O(m*n)
        # space: O(n)
        dp = [ [False for i in range(len(p)+1)] for j in range(len(s) + 1) ]
        dp[0][0] = True
        
        for i in range(2, len(p)+1):
            dp[0][i] = (p[i-1] == '*') and dp[0][i-2]
        
        for i in range(1, len(s)+1):
            dp[i][0] = False
        
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j] 
                else:
                    if (s[i - 1] == p[j - 1] or p[j - 1] == '.') and (j >= len(p) or p[j] != '*') :
                        dp[i][j] |= dp[i - 1][j-1]
                    
        
        return dp[-1][-1]