class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        s = '[' + s + ']'
        stack = []
        
        ptr = 0
        while ptr < len(s):
            char = s[ptr]
            
            if char.isdigit():
                count = ""
                while ptr < len(s) and s[ptr].isdigit():
                    count += s[ptr]
                    ptr += 1
                    
                stack.append(count)
                continue
            
            if char.isalpha():
                seq = ""
                while ptr < len(s) and s[ptr].isalpha():
                    seq += s[ptr]
                    ptr += 1
                    
                stack.append(seq)
                continue
                
            if char == ']':
                sub_str = ""
                while stack and not stack[-1].isdigit():
                    sub_str = stack.pop() + sub_str
                
                k = int(stack.pop()) if stack else 1
                stack.append(k * sub_str)
                 
            ptr += 1
            
        return stack.pop() if stack else None
                