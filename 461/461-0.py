class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = x ^ y
        
        counter = 0
        while result > 0:
            last_bit = result & 1
            result = result >> 1
            if last_bit == 1:
                counter += 1
        
        return counter
        
        