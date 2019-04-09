class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        
        if not s:
            return True
        
        if not t:
            return False
        
        if len(s) > len(t):
            return False
        
        i = 0 
        j = 0
        while i < len(s):
            if j == len(t):
                return False
            
            while j < len(t) and t[j] != s[i]:
                j += 1
                
            if j < len(t):
                i += 1
                j += 1
                
        return True