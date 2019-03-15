class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
                
        if i >= j:
            return True
        
        ans = False
        if s[j - 1] == s[i]:
            ans |= self.helper(i, j - 1, s)
            
        if s[i + 1] == s[j]:
            ans |= self.helper(i + 1, j, s)
            
        return ans
    
    def helper(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
        