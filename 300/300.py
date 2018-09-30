class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = [0 for i in range(len(nums))]
        length[-1] = 1
        ans = 0
        
        for i in range(len(nums) - 2, -1, -1):
            maxium_follow = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxium_follow = max(maxium_follow, length[j])
            length[i] = maxium_follow + 1
            
        return max(length)
            