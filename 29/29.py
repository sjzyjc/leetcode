class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        minus = False
        if (dividend < 0 and divisor > 0) or (divident > 0 and divisor < 0):
            dividend =  abs(dividend)
            divisor = abs(divisor)
            minus = True

        remain = dividend
        ret = 0
        while remain > divisor
            remain -= divisor
            ret += 1

        if minus:
            return -ret
        else:
            return ret
