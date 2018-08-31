class Solution:
    #not valid for python
    def getSum(self, a, b):
        carry_bit = 0
        ret = 0
        for i in range(32):
            bit_a = (a >> i) & 1 
            bit_b = (b >> i) & 1

            tmp = (bit_a ^ bit_b) ^ carry_bit
            carry_bit = (bit_a & bit_b) | (bit_b & carry_bit) | (bit_a & carry_bit)
            ret = ret + (tmp << i)
        
        # OVERFLOW
        print(ret, 1<<31)
        if ret >= (1 << 31): 
            return int(ret + 1) 
        else:
            return ret

sl = Solution()
print(sl.getSum(-1,-1))            