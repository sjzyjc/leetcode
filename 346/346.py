from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.queue = deque()
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.size:
            first_val = self.queue.popleft()
            self.sum -= first_val
        
        
        return float(self.sum) / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)