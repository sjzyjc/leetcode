class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        s = s + '$'
        stack, num, operator = [], "", '+'
        for charr in s:
            #print(charr)
            if charr.isdigit():
                num += charr
            elif charr == ' ':
                continue
            else: #operand
                if operator == '+':
                    stack.append(int(num))
                elif operator == '-':
                    stack.append(-int(num))
                elif operator == '*':
                    stack.append(stack.pop() * int(num))
                else:
                    last_expression = stack.pop()
                    if last_expression // int(num) < 0:
                        stack.append(-(-last_expression // int(num)))
                    else:
                        stack.append(last_expression // int(num))
                        
                
                #print(stack)
                operator = charr
                num = ""
                
        return sum(stack)
                        
                        
                    
                
        