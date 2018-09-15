class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not num or len(num) <= k:
            return "0"
        
        stack = []
        counter = 0
        for char in num:    
            while stack and counter < k and int(char) < stack[-1]:
                stack.pop()
                counter += 1
                
            stack.append(int(char))
        
        if counter < k:
            stack = stack[:len(stack) - (k - counter)]
        
        ret = 0
        for num in stack:
            ret = ret * 10 + num
        
        return str(ret)