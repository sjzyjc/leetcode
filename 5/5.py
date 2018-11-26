class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        ans = ""
        
        for i in range(len(s)):
            #odd
            tmp_ans = s[i]
            for j in range(1, len(s)):
                if i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                    tmp_ans = s[i - j : i + j + 1]
                else:
                    break
                    
            if len(tmp_ans) > len(ans):
                ans = tmp_ans
            
            #even
            tmp_ans = ""
            for j in range(0, len(s)):
                if i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + 1 + j]:
                    tmp_ans = s[i - j : i + j + 1 + 1]
                else:
                    break
                 
            if len(tmp_ans) > len(ans):
                ans = tmp_ans
            
        return ans
                    