class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        pair = {')':'(', ']':'[', '}':'{'}
        for charr in s:
            if charr in ['(', '{', '[']:
                stack.append(charr)
            else:
                if not stack or stack[-1] != pair[charr]:
                    return False
                
                stack.pop()
                
        return len(stack) == 0
        