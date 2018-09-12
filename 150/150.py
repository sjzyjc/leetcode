class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                operand1, operand2 = stack.pop(), stack.pop()
                if token == "+":
                    result = operand1 + operand2
                if token == "-":
                    result = operand2 - operand1
                if token == "*":
                    result = operand1 * operand2
                if token == "/":
                    if (operand1 > 0 and operand2 < 0) or (operand1 < 0 and operand2 > 0):
                        result = - ((-operand2) // operand1)
                    else:
                        result = operand2 // operand1
                        
                stack.append(result)
        
        return stack[-1]