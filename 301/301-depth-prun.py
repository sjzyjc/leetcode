class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        ans = []
        self.dfs(s, ans, 0, 0, ['(', ')'])
        return ans
    
    def dfs(self, s, ans, ptr, next_remove, pair):
        unmatched = 0
        for i in range(ptr, len(s)):
            if s[i] == pair[0]:
                unmatched += 1
                
            if s[i] == pair[1]:
                unmatched -= 1
                
            if unmatched >= 0:
                continue
                
            #invalid
            for j in range(next_remove, i + 1):
                if j > 0 and s[j] == s[j - 1]:
                    continue
                    
                if s[j] != pair[1]:
                    continue
                    
                self.dfs(s[:j] + s[j+1:], ans, i, j, pair)
            
            return
        
        if pair[0] == '(':
            self.dfs(s[::-1], ans, 0, 0, [')', '('])
        else:
            #print("append", s[::-1])
            ans.append(s[::-1])
            
            
                
                