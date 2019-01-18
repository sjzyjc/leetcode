from collections import deque
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        self.index = 0
        return self.dfs(s)
    
    def dfs(self, s):
        if self.index >= len(s):
            return ""
        
        if s[self.index] == '[': self.index += 1
            
        
        sub_str = ""
        while self.index < len(s) and s[self.index] != ']':
            char = s[self.index]
            if char.isalpha():
                seq = ""
                while self.index < len(s) and s[self.index].isalpha():
                    seq += s[self.index]
                    self.index += 1
                
                sub_str += seq 
                
            elif char.isdigit():
                count = ""
                while self.index < len(s) and s[self.index].isdigit():
                    count += s[self.index]
                    self.index += 1
            
                if count: sub_str += int(count) * self.dfs(s)
            
            else:
                self.index += 1    
        
        if self.index < len(s): self.index += 1
        return sub_str
        