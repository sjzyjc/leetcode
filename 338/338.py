class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num <= 0:
            return [0]
        
        count = [0 for i in range(num + 1)]
        count[0] = 0
        
        for i in range(1, num + 1):
            count[i] += count[i >> 1] + (i % 2)
            
        return count