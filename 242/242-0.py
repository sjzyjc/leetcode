class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (s is None) != (t is None):
            return False
        
        if len(s) != len(t):
            return False
        
        hash_map = {i:0 for i in t}
        for char in t:
            hash_map[char] += 1
        
        source_map = {j: 0 for j in s}
        for char in s:
            source_map[char] += 1
        
        for key in hash_map:
            if key not in source_map:
                return False
            if hash_map[key] != source_map[key]:
                return False
            
        return True