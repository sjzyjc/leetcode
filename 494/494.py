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
        
        f = [[0 for j in range(2 * total + 1)] for i in range(len(nums) + 1)]
        f[0][total] = 1
        
        for i in range(1, len(nums) + 1):
            for j in range(2 * total + 1):
                if 0 <= j - nums[i - 1] < 2 * total + 1:
                    f[i][j] += f[i - 1][j - nums[i - 1]] 
                    
                if 0 <= j + nums[i - 1] < 2 * total + 1:
                    f[i][j] += f[i - 1][j + nums[i - 1]]
                
        #print(f)
        return f[-1][S  + total]