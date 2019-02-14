class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        if not str:
            return []
        
        is_palin = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            #aba
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                is_palin[i - j][i + j] = True
                j += 1
            
            #abba
            j = 0
            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                is_palin[i - j][i + 1 + j] = True
                j += 1
                
        ans = []
        self.helper(s, 0, [], ans, is_palin)
        return ans
    
    def helper(self, s, start, carry, ans, is_palin):
        if start == len(s):
            ans.append(carry + [])
            return
        
        for i in range(start, len(s)):
            if not is_palin[start][i]:
                continue
                
            carry.append(s[start:i + 1])
            self.helper(s, i + 1, carry, ans, is_palin)
            carry.pop()
            
            
            
        
        