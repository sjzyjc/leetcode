class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums) - 1:
            ans += nums[i]
            i += 2
            
        return ans