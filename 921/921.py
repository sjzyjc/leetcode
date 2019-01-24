class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        
        left, right = 0, 0
        for char in S:
            if char == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1
                    
        return left + right
            