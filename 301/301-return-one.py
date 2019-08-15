class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        stack = []
        ans = ''
        for charr in s:
            if charr != ')':
                stack.append(charr)
            else:
                tmp = ''
                while stack and stack[-1] != '(':
                    tmp = stack.pop() + tmp
                    
                    
                if stack and stack[-1] == '(':
                    tmp = stack.pop() + tmp
                    
                if tmp:
                    ans += tmp + ')'
                    
                    
        return ans
                
            
            
            
        