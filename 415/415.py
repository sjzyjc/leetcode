class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2:
            return 0
        
        stack1, stack2 = [], []
        for char in num1:
            stack1.append(char)
            
        for char in num2:
            stack2.append(char)
            
        carry = 0
        ans = ""
        while stack1 or stack2 or carry:
            if stack1:
                carry += (ord(stack1.pop()) - ord('0'))
                
            if stack2:
                carry += (ord(stack2.pop()) - ord('0'))
                
            ans = str(carry % 10) + ans
            carry //= 10
            
        return ans