from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.arr = deque([])
        

    def next(self, val: int) -> float:
        self.sum += val
        self.arr.append(val)
        if len(self.arr) > self.size:
            self.sum -= self.arr.popleft()
            
        return self.sum / len(self.arr)