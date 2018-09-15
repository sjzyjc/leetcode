class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reverse_stack = []
        self.first = None
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.first = x
            
        self.stack.append(x)
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.reverse_stack) == 0:
            while self.stack:
                self.reverse_stack.append(self.stack.pop())
            
        return self.reverse_stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.reverse_stack:
            return self.reverse_stack[-1]
                
        return self.first

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0 and len(self.reverse_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()