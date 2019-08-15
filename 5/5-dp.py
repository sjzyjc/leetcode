class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        ans = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            
        for i in range(len(s) - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            if dp[i][i + 1]:
                ans = s[i : i + 2]
            
        for l in range(2, len(s)):
            for i in range(len(s) - l):
                dp[i][i + l] |= dp[i + 1][i + l - 1] and (s[i] == s[i + l])
                
                if dp[i][i + l]:
                    ans = s[i : i + l + 1]
            
        #print(dp)
        return ans
                    