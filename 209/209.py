class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        
        i = 0
        ans = len(nums)
        tmp = 0
        for j in range(len(nums)):
            tmp += nums[j]
            while tmp - nums[i] >= s:
                tmp -= nums[i]
                i += 1
            
            if tmp >= s:
                ans = min(ans, j - i + 1)
                
        return ans
        
            
        