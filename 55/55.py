class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        f = [False for i in range(len(nums))]
        f[0] = True
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if f[j] and j + nums[j] >= i:
                    f[i] = True
                    break
        return f[-1]