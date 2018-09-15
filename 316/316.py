class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        remain = {i : 0 for i in s}
        for char in s:
            remain[char] += 1
            
        stack = []
        used = {i:False for i in s}
       
        for char in s:
            remain[char] -= 1
            if used[char]:
                continue
                
            while stack and ord(char) < ord(stack[-1]) and remain[stack[-1]] >= 1:
                large = stack.pop()
                used[large] = False
            
            stack.append(char)
            used[char] = True
        
        return "".join(stack)
        