class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        f = [0 for i in range(len(s) + 1)]
        f[0] = 1
        
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            
            if i >= 2 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                f[i] += f[i - 2]
        
        return f[len(s)]