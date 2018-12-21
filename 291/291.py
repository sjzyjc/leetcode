class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str:
            return True
        
        if not pattern or not str:
            return False
        
        return self.helper(pattern, str, 0, 0, {})
    
    def helper(self, pattern, word, p_index, s_index, word_map):
        if p_index == len(pattern) and s_index == len(word):
            return True
        
        if p_index == len(pattern) or s_index == len(word):
            return False
        
        p = pattern[p_index] + '$'
        if p not in word_map:
            for i in range(s_index, len(word)):
                sub_word = word[s_index: i + 1]
                if sub_word in word_map:
                    continue
                    
                word_map[p] = sub_word
                word_map[sub_word] = p
                if self.helper(pattern, word, p_index + 1, i + 1, word_map):
                    return True
                
                del word_map[p]
                del word_map[sub_word]
        else:
            if word[s_index :].startswith(word_map[p]) and self.helper(pattern, word, p_index + 1, s_index + len(word_map[p]), word_map):
                return True
            
        return False
        
        