class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_sum = - (1 << 31)
        min_prefix = cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum - min_prefix, max_sum)
            min_prefix = min(min_prefix, cur_sum)
        
        return max_sum
            
            