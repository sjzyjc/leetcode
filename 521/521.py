class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if not a and not b:
            return -1
        
        if not a:
            return len(b)
        
        if not b:
            return len(a)
        
        if a != b:
            return max(len(a), len(b))
            
        return -1