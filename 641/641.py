class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.arr = [-1 for _ in range(k)]
        self.start = 0
        self.end = 0
        self.k = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
     
            
        self.arr[self.start % self.k] = value 
        if self.start == self.end:
            self.end += 1
            
        self.start -= 1
        
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.arr[self.end % self.k] = value
        
        if self.end == self.start:
            self.start -= 1
            
        self.end += 1
        
        return True
        
        
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.arr[(self.start - 1) % self.k] = -1
        self.start += 1
        
        if self.start + 1 == self.end:
            self.end = self.start
            
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.arr[(self.end - 1) % self.k] = -1
        self.end -= 1
        
        if self.end == self.start + 1:
            self.start = self.end
            
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.arr[(self.start + 1) % self.k]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.arr[(self.end - 1) % self.k]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.start == self.end
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.end - self.start - 1 == len(self.arr)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()