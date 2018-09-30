class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = len(nums)
        maximum = [ - (1 << 31) for i in range(length)]
        minimum = [(1 << 31) - 1 for i in range(length)]
        ans = nums[-1]
        
        maximum[-1] = nums[-1]
        minimum[-1] = nums[-1]
        
        for i in range(length - 2, -1, -1):
            if nums[i] < 0:
                maximum[i] = max(nums[i], nums[i] * minimum[i + 1])
                minimum[i] = min(nums[i], nums[i] * maximum[i + 1])
                
            else:
                maximum[i] = max(nums[i], nums[i] * maximum[i + 1])
                minimum[i] = min(nums[i], nums[i] * minimum[i + 1])
                
            if maximum[i] > ans:
                ans = maximum[i]
               
        return ans
                
        
        