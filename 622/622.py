class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [-1 for _ in range(k)]
        self.size = k
        self.start = 0
        self.end = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.queue[self.end % self.size] = value
        self.end += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.queue[self.start % self.size] = -1
        self.start += 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.queue[self.start % self.size]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.queue[(self.end - 1) % self.size]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.end == self.start

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.end - self.start == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()