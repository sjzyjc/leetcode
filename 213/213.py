class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums, 0, len(nums) -2), self.helper(nums, 1, len(nums) - 1))
        

    def helper(self, nums, start, end):
        pre_prev = 0
        prev = 0
        ans = 0
        for index in range(start, end + 1):
            ans = max(nums[index] + pre_prev, prev)
            pre_prev = prev
            prev = ans
        
        return ans 
        
        