class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        
        str = str.strip()
        sign = None
        number = ''
        for index, charr in enumerate(str):
            if (charr == '-' or charr == '+') and index == 0:
                sign = charr
                
            elif charr.isdigit():
                number += charr
            else:
                break
                
        if len(number) == 0:
            return 0
        
        res = 0
        for digit in number:
            val = ord(digit) - ord('0')
            res *= 10
            res += val
            
        if sign and sign == '-':
            res = -res
            
        if res < -(1 << 31):
            return -(1 << 31)
        
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
            
        return res
            