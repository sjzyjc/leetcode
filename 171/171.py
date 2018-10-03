class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        ans = 0
        for char in s:
            ans = ans * 26 + (ord(char) - ord('A') + 1)
        
        return ans