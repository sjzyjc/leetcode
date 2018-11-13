from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.copy = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        ans = None
        while self.queue:
            if len(self.queue) == 1:
                ans = self.queue.popleft()
                continue
            self.copy.append(self.queue.popleft())
            
        self.queue, self.copy = self.copy, self.queue
        return ans
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        ans = None
        while self.queue:
            if len(self.queue) == 1:
                ans = self.queue[0]
            self.copy.append(self.queue.popleft())
        
        self.queue, self.copy = self.copy, self.queue
        return ans
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()