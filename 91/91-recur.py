class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        return self.dfs(s, 0, {})
    
    def dfs(self, s, start_index, memo):
        if start_index == len(s):
            return 1
        
        if start_index in memo:
            return memo[start_index]
        
        ans = 0
        if s[start_index] != '0':
            ans += self.dfs(s, start_index + 1, memo)
        
        if start_index + 1 < len(s) and (s[start_index] == '1' or (s[start_index] == '2' and 0 <= ord(s[start_index + 1]) - ord('0') <= 6)):
            ans += self.dfs(s, start_index + 2, memo)
            
        memo[start_index] = ans
        return ans