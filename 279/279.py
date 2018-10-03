from collections import deque
import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = deque([n])
        level = -1
        
        while queue:
            length = len(queue)
            level += 1
            
            for i in range(length):
                remain = queue.popleft()
                
                sqrt = int(math.sqrt(remain))

                for i in range(sqrt, 0, -1):
                    if remain - (i * i) == 0:
                        return level + 1
                    queue.append(remain - (i * i))
        
        return -1
                
                