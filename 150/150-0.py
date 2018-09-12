class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            stack.append(token)
            
        self.helper(stack)
        return int(stack[-1])
    
    def helper(self, stack):
        if len(stack) == 0:
            return
        
        if stack[-1] not in ["+", "-", "*", "/"]:
            return 
        
        result = 0
        operators = [stack.pop()]
        while stack and operators:
            while stack[-1] in ["+", "-", "*", "/"]:
                operators.append(stack.pop())
            
            operand1 = int(stack.pop())
            self.helper(stack)
            operand2 = int(stack.pop())
            
            operator = operators.pop()
            print(operand1, operand2, operator)
            if operator == "+":
                result = operand1 + operand2
            
            if operator == "-":
                result = operand2 - operand1
            
            if operator == "*":
                result = operand1 * operand2
                
            if operator == "/":
                if operand2 * operand1 < 0:
                    result =  - (-operand2 // operand1)
                else:
                    result = operand2 // operand1     
                
            stack.append(result)
            
            
           
                
                
             
        
            
        