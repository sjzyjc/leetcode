class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for charr in s:
            if charr in ['(', '{', '[']:
                stack.append(charr)
            else:
                if charr == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                        
                if charr == '}':
                    if not stack or stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                        
                if charr == ']':
                    if not stack or stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                        
        return len(stack) == 0
            
                