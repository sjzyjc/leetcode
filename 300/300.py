class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        f = [1 for i in range(len(nums))]
        maximum = - (1 << 31)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                    
                f[i] = max(f[i], f[j] + 1)
                
            maximum = max(f[i], maximum)
                
        return maximum
            
        