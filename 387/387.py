class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        
        count_map = {}
        
        for char in s:
            if char not in count_map:
                count_map[char] = 1
            else:
                count_map[char] += 1
            
        for index in range(len(s)):
            if count_map[s[index]] == 1:
                return index
            
        return -1
                