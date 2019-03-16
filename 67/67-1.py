class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        
        if not b:
            return a
        
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1
        carry = False
        
        ans = ""
        while ptr1 >= 0 or ptr2 >= 0 or carry:
            operand_1 = int(a[ptr1]) if ptr1 >= 0 else 0  
            operand_2 = int(b[ptr2]) if ptr2 >= 0 else 0
                        
            res = operand_1 ^ operand_2 ^ carry
            carry = (operand_1 & carry) | (operand_2 & carry) | (operand_1 & operand_2) 
              
            ans += str(res)
            ptr1 -= 1
            ptr2 -= 1
            
        return ans[::-1]
                