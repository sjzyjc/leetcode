class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        ans = []
        self.dfs(s, 0, ans, [])
        return ans
    
    def dfs(self, s, s_index, ans, carry):
        if len(carry) == 4 and s_index < len(s):
            return
        
        if s_index == len(s):
            if len(carry) == 4:
                ans.append('.'.join(carry))
            return
        
        for i in range(s_index, min(s_index + 3, len(s))):
            if s[s_index] == '0' and i != s_index:
                break
                
            num = int(s[s_index : i + 1])
            if not (0 <= num <= 255):
                break
                
            carry.append(str(num))
            self.dfs(s, i + 1, ans, carry)
            carry.pop()
                
            
        