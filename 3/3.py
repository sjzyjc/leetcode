class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        ans = 0
        i = 0
        hash_map = {}
        for j in range(len(s)):
            char = s[j]
            if char in hash_map and hash_map[char] >= i:
                i = hash_map[char] + 1
            
            ans = max(ans, j - i + 1)
            hash_map[char] = j
            
        return ans
            