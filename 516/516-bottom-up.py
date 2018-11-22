class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        f = [[1 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] += 1
                
        for l in range(3, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                    continue
                
                f[i][j] = max(f[i][j - 1], f[i + 1][j])
                
        return f[0][-1]