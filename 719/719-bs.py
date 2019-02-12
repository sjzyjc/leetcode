class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or not k:
            return -1
        
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        
        while start < end:
            mid = start + (end - start) // 2
            if self.countLessEqual(nums, mid) < k:
                start = mid + 1
            else:
                end = mid
                
        return start
    
    def countLessEqual(self, nums, target):
        j = 0
        ans = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= target:
                j += 1
                
            ans += max(0, j - 1 - i)
                
        return ans
                
            
        
        