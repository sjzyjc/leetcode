class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None or len(nums) == 0:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        ans = [-1, -1]
        
        ans[0] = self.findFirstGreaterOrEqual(nums, target, False)
        
        if ans[0] == -1:
            return ans
        
        ans[1] = self.findFirstGreaterOrEqual(nums, target + 1, True)

        return ans
    
    def findFirstGreaterOrEqual(self, nums, target, left):
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
                
        if not left:
            if nums[start] == target:
                return start
            else:
                return -1
            
        #finding rightmost
        if nums[start] >= target: 
            return start - 1
        else:
            return len(nums) - 1
        