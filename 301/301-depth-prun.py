class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        
        unmatched = 0
        invalid_right = 0
        for charr in s:
            if charr == '(':
                unmatched += 1
            
            if charr == ')':
                unmatched -= 1
                
            if unmatched < 0:
                invalid_right += 1
                unmatched = 0
                
        
        ans = []
        self.helper(s, unmatched, invalid_right, 0, ans)
        return ans
    
    def helper(self, s, l, r, start, ans):
        #print(s, l, r, start, ans)
        if self.isValid(s) and l == 0 and r == 0:
            ans.append(s)
            return
        
        for index in range(start, len(s)):
            if index > 0 and s[index] == s[index - 1]:
                continue
                
            if l > 0 and s[index] == '(':
                self.helper(s[:index] + s[index + 1:], l-1, r, index, ans)
            
            if r > 0 and s[index] == ')':
                self.helper(s[:index] + s[index + 1:], l, r-1, index, ans)
                
    
    def isValid(self, s):
        unmatched = 0
        invalid = 0
        for char in s:
            if char == '(':
                unmatched += 1
                
            if char == ')':
                unmatched -= 1
                
            if unmatched < 0:
                invalid += 1
                unmatched = 0
                
        return (invalid + unmatched) == 0
            
                
            
        
        

