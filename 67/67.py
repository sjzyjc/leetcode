class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry_bit = 0
        ret = 0
        for i in range(32):
            bit_a = (a >> i) & 1 
            bit_b = (b >> i) & 1

            tmp = (bit_a ^ bit_b) ^ carry_bit
            carry_bit = (bit_a & bit_b) | (bit_b & carry_bit) | (bit_a & carry_bit)

            ret += tmp << i 

        return ret     

sl = Solution()
print(sl.addBinary(101,1))            