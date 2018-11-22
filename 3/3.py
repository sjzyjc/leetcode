class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        
        max_sub = 0
        left, right = 0, 0
        hash_map = {}
        
        while right < len(s):
            char = s[right]
            if char in hash_map and hash_map[char] >= left:
                # find dup
                max_sub = max(max_sub, right - left)
                left = hash_map[char] + 1

            hash_map[char] = right
            right += 1
                        
        return max(max_sub, right - left)
                
            
            
                