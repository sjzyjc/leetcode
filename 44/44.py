class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (not s and not (not p or p == "*")) or (s and not p):
            return False
        
        if (not s and not p) or (not s and p == "*"):
            return True
        
        match = [[-1 for i in range(len(p))] for j in range(len(s))]
        self.helper(s, p, 0, 0, match)
        return match[0][0]
    
    def helper(self, s, p, s_index, p_index, match):
        if s_index == len(s) and p_index == len(p):
            return True        
        
        if s_index == len(s) and p_index != len(p):
            return self.isEmptyP(p, p_index)
            
        if p_index == len(p) and s_index != len(s):
            return False
        
        if match[s_index][p_index] != -1:
            return match[s_index][p_index]
        
        is_match = False
        if p[p_index] == '*':
            is_match = self.helper(s, p, s_index, p_index + 1, match) or self.helper(s, p, s_index + 1, p_index, match)
        elif p[p_index] == '?':
            is_match = self.helper(s, p, s_index + 1, p_index + 1, match)
        else:
            is_match = (s[s_index] == p[p_index]) and self.helper(s, p, s_index + 1, p_index + 1, match)
            
        match[s_index][p_index] = is_match
        return match[s_index][p_index]
        
    def isEmptyP(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
            
        return True