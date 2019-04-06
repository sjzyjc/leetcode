class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        ptr, stack, last_op = 0, [], '+'

        s = '(' + s + ')'
        while ptr < len(s):
            charr = s[ptr]
            if charr == ' ':
                ptr += 1
                continue
                
            if charr.isdigit():
                tmp = ""
                while ptr < len(s) and s[ptr].isdigit():
                    tmp += s[ptr]
                    ptr += 1
                    
                self.eval(last_op, int(tmp), stack)
                continue
                
            if charr == '(':
                stack.append(last_op)
                last_op = '+'
            elif charr == ')':
                tmp_sum = 0
                while isinstance(stack[-1], int):
                    tmp_sum += stack.pop()
                    
                op = stack.pop() if stack else '+'
                self.eval(op, tmp_sum, stack)
                
            else:
                last_op = charr
                
            ptr += 1
                
        return stack[-1]
        
    def eval(self, op, second, stack):
        if op == '+':
            stack.append(second)
        elif op == '-':
            stack.append(-second)
        elif op == '*':
            stack.append(stack.pop() * second)
        else:
            last_expr = stack.pop()
            if last_expr // second < 0:
                stack.append(-(-last_expr // second))
            else:
                stack.append(last_expr // second)
        