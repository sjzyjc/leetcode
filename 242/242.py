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
        
        counter = [0 for i in range(ord('a'), ord('z') + 1)]
        for i in range(len(t)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for i in counter:
            if i != 0:
                return False
            
        return True