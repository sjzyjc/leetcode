class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        count = 1
        ans = count
        
        for index, num in enumerate(nums):
            if index == 0:
                continue
                
            if num > nums[index - 1]:
                count += 1
            elif num <= nums[index - 1]:
                if count > ans:
                    ans = count
                count = 1
                
            if index == len(nums) - 1:
                ans = max(ans, count)
                
        return ans
                