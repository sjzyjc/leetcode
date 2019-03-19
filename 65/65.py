class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        
        has_e = False
        has_sign = False
        has_dot = False
        has_digit = False
        
        s = s.strip()
        if not s:
            return False
        
        for index, charr in enumerate(s):
            if charr not in ['+', '-', '.', 'e'] and not charr.isdigit():
                return False
            
            if charr == '+' or charr == '-':
                if not (index == 0 or s[index - 1] == 'e'):
                    return False
                else:
                    has_sign = True
            
            if charr == 'e':
                if has_e or not has_digit:
                    return False
                else:
                    has_e = True
                    has_sign = False
                    has_digit = False
                    
            if charr == '.':
                if has_dot or has_e:
                    return False
                else:
                    has_dot = True
                    
            if charr.isdigit():
                has_digit = True
                
        if (has_dot or has_e or has_sign) and not has_digit:
            return False
        
        return True
                    
                
                    
            
                
                
                
                
                