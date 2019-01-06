class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        
        sign = ""
        num = ""
        start_parse = False
        for char in str:
            if char == ' ' and not start_parse:
                continue
            
            if (char == '+' or char == '-') and not start_parse:
                sign = char
                start_parse = True
                continue
                
            if char.isdigit():
                num += char
                if not start_parse:
                    start_parse = True
            else:
                break
                    
        #print(sign, num)
        if len(num) == 0:
            return 0
        
        if sign == '-':
            return max(-int(num),  - 1 << 31)
        
        return min(int(num), (1 << 31) - 1)
        
                
        
        