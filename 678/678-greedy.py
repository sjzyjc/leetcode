class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        upper = lower = 0
        for charr in s:
            if charr == '(':
                upper += 1
                lower += 1
            elif charr == ')':
                upper -= 1
                lower = max(0, lower - 1)
                    
                if upper < 0:
                    return False
                
            else:
                upper += 1
                lower = max(0, lower - 1)
                
        return lower == 0
            
            
        