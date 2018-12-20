class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and (not p or self.isValidP(p, 0)):
            return True
        
        if not p:
            return False
        
        if not s and (p or not self.isValidP(p, 0)):
            return False
        
        match = [[-1 for i in range(len(p))] for j in range(len(s))]
        self.helper(s, p, 0, 0, match)
        return match[0][0]
    
    def helper(self, s, p, s_index, p_index, match):
        if s_index == len(s) and p_index == len(p):
            return True
        
        if s_index == len(s):
            return self.isValidP(p, p_index)
        
        if p_index == len(p):
            return False
        
        if match[s_index][p_index] != -1:
            return match[s_index][p_index]
        
        is_match = False 
        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            if s[s_index] == p[p_index] or p[p_index] == ".":
                is_match = self.helper(s, p, s_index, p_index + 2, match) or self.helper(s, p, s_index + 1, p_index, match)
            else:
                is_match = self.helper(s, p, s_index, p_index + 2, match)
        else:
            is_match = (s[s_index] == p[p_index] or p[p_index] == ".") and self.helper(s, p, s_index + 1, p_index + 1, match)
        
        match[s_index][p_index] = is_match
        return match[s_index][p_index]
            
            
    def isValidP(self, p, p_index):
        if (len(p) - p_index) % 2 == 1:
            return False
        
        for i in range(p_index, len(p) - 1, 2):
            if p[i + 1] != "*":
                return False
        return True
            