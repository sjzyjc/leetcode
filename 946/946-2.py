class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed and not popped:
            return True
        
        if len(pushed) != len(popped):
            return False
        
        i = 0
        arr = []
        for index, num in enumerate(pushed):
            top  = index
            
            while top >= 0 and i < len(popped):
                if pushed[top] == popped[i]:
                    pushed[top] = '#'
                    top -= 1
                    i += 1
                elif pushed[top] == '#':
                    top -= 1
                else:
                    break
                    
        return i == len(popped)
        