class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        count = 0
        
        for i in range(len(s)):
            count += 1
            j = 1
            #aba
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                count += 1
                j += 1
                
            #aabb
            j = 0
            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                count += 1
                j += 1
                
        return count
            