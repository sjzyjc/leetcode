class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        s = '(' + s + ')'
        stack = []
        ptr = 0
        prev_sign = '+'
        
        while ptr < len(s):
            char = s[ptr]
            #print(stack, char, ptr)
            if char == ')':
                tmp_sum = 0
                while stack and stack[-1] != '+' and stack[-1] != '-':
                    tmp_sum += stack.pop()
                    
                sign = stack.pop() if stack else '+'
                if sign == '-':
                    tmp_sum = -tmp_sum
                
                stack.append(tmp_sum)
                
            elif char.isdigit():
                tmp_int = ""
                while ptr < len(s) and s[ptr].isdigit():
                    tmp_int += s[ptr]
                    ptr += 1
                
                if prev_sign == '+':
                    stack.append(int(tmp_int))
                else:
                    stack.append(-int(tmp_int))
                    
                continue
                    
            elif char == '+' or char == '-':
                prev_sign = char
            
            elif char == '(':
                stack.append(prev_sign)
                prev_sign = '+'
                    
            ptr += 1
            
        return stack[-1]
                    
                    
        