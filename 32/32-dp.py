class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        f = [0 for _ in range(len(s) + 1)]
        ans = 0
        
        for i in range(1, len(s) + 1):
            if i < 2 or s[i - 1] == '(':
                continue
            
            if s[i - 2] == '(':
                f[i] = f[i - 2] + 2
                
            else:
                if i - f[i - 1] - 2 >= 0 and s[i - f[i - 1] - 2] == '(':
                    f[i] = f[i - 1] + 2 + f[i - f[i - 1] - 2]
                    
                    
            ans = max(ans, f[i])
            
        #print(f)
        return ans
            
        
        