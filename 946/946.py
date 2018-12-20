class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) != len(popped):
            return False
        
        i = 0
        arr = []
        for num in pushed:
            arr.append(num)
            
            while arr and arr[-1] == popped[i]:
                arr.pop()
                i += 1
                
        return len(arr) == 0
        