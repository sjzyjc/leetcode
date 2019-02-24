class Solution:
    def shortestPalindrome(self, s: 'str') -> 'str':
        if not s:
            return ""
        
        half = len(s) // 2
        ans = ""
        for i in range(len(s) - half, -1, -1):
            #central is char
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            
            if i + j <= len(s) and i - j < 0:
                sub_str = s[i + j : ]
                ans = sub_str[::-1] + s
                return ans
                
            #central is line
            j = 0
            while i - 1 - j >= 0 and i + j < len(s) and s[i - 1 - j] == s[i + j]:
                j += 1
                
            if i + j <= len(s) and i - 1 - j < 0:
                sub_str = s[i + j : ]
                ans = sub_str[::-1] + s
                return ans
                
        
        return ans
                
                
        