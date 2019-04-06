class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        return self.dfs(s, 0, 0)
    
    def dfs(self, s, s_index, unmatched):
        if unmatched < 0:
            return False
        
        
        for index in range(s_index, len(s)):
            charr = s[index]
            if charr == '(':
                unmatched += 1
                
            elif charr == ')':
                unmatched -= 1
                if unmatched < 0:
                    return False
                
            else:
                if self.dfs(s, index + 1, unmatched + 1) or self.dfs(s, index + 1, unmatched) or self.dfs(s, index + 1, unmatched - 1):
                    return True
                
        
        return unmatched == 0
            
            
        