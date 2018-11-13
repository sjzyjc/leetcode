class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        dup_set = set()
        for charr in s:
            if charr not in dup_set:
                dup_set.add(charr)
            else:
                dup_set.remove(charr)
                
        
        return len(dup_set) <= 1
            