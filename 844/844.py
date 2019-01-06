class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S is None and T is None:
            return True
        
        if (S is None) != (T is None):
            return False
        
        stack1 = []
        stack2 = []
        for char in S:
            if char == '#':
                if stack1:
                    stack1.pop()
                continue
            
            stack1.append(char)
            
        for char in T:
            if char == '#':
                if stack2:
                    stack2.pop()
                continue
            
            stack2.append(char)
        
        return stack1 == stack2
        