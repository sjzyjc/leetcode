from collections import deque
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
                sqrt = int(remain ** (1/2))

                for i in range(sqrt, 0, -1):
                    if remain - (i ** 2) == 0:
                        return level + 1
                    queue.append(remain - (i**2))
        
        return -1
                
                