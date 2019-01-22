class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums: 
            return 0
        
        total = sum(nums)
        if S > total or S < -total:
            return 0
        
        return self.helper(nums, S, {}, len(nums))
    
    def helper(self, nums, target, memo, ptr):
        if (ptr, target) in memo:
            return memo[(ptr, target)]
        
        if ptr == 0:
            if target == 0:
                return 1
            else:
                return 0
            
        ans = self.helper(nums, target - nums[ptr - 1], memo, ptr - 1) + self.helper(nums, target + nums[ptr - 1], memo, ptr - 1)
        memo[(ptr, target)] = ans
        return ans
        