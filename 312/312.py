class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums = [1] + nums + [1]
        f = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for length in range(3, len(nums) + 1):
            for i in range(len(nums) - length + 1): 
                j = i + length - 1
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + nums[i] * nums[k] * nums[j])
                    
        return f[0][-1]
                        