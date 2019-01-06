class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0 for _ in range(len(nums))]
        self.bit = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.update(i, nums[i])

        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        
        while i < len(self.bit):
            self.bit[i] += delta
            i += self.lowbit(i)
       

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum(j) - self.prefixSum(i - 1)
        
    def prefixSum(self, i):
        ans = 0
        i = i + 1
        while i > 0:
            ans += self.bit[i]
            i -= self.lowbit(i)

        return ans
    
    def lowbit(self, x):
        return x & -x
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)