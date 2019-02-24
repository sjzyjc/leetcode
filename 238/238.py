class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        ans = [1 for _ in range(len(nums))]
        prefix_product = 1
        for i in range(1, len(nums)):
            prefix_product *= nums[i - 1]
            ans[i] = prefix_product
            
        suffix_product = 1 
        for i in range(len(nums) - 2, -1, -1):
            suffix_product *= nums[i + 1]
            ans[i] *= suffix_product
            
        return ans
            
            
        