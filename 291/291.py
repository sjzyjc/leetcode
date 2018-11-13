class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or str is None:
            return False
        
        return self.helper(pattern, str, 0, 0, {})
    
    def helper(self, pattern, str, p_index, s_index, cur_dict):
        if p_index == len(pattern) and s_index == len(str):
            return True
        
        if p_index == len(pattern) or s_index == len(str):
            return False
        
        p = pattern[p_index] + "$"
        if p not in cur_dict:
            for i in range(s_index, len(str)):
                word = str[s_index: i + 1]
                if word in cur_dict:
                    continue
                
                cur_dict[p] = word
                cur_dict[word] = cur_dict[p]
                if self.helper(pattern, str, p_index + 1, i + 1, cur_dict):
                    return True
                del cur_dict[p]
                del cur_dict[word]
        else:
            if not str[s_index :].startswith(cur_dict[p]):
                return False
            
            if self.helper(pattern, str, p_index + 1, s_index + len(cur_dict[p]), cur_dict):
                return True
        
        return False
                
    