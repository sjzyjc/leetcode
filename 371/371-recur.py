class Solution:
    def getSum(self, a, b):
        if b == 0:
            return a

        return self.getSum(a^b, (a & b) << 1)

sl = Solution()
print(sl.getSum(1,2))
print(sl.getSum(-1,-1))
