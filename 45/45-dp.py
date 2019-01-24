class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_int = (1 << 31) - 1
        f = [max_int for _ in range(len(nums))]
        f[0] = 0
        
        for i in range(1, len(nums)):
            for j in range(i):
                if f[j] != max_int and j + nums[j] >= i:
                    f[i] = min(f[j] + 1, f[i])
                    
        return f[-1]
                    
            