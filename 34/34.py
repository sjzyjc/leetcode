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
        
        #leftmost
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        if nums[start] == target:
            ans[0] = start
            
        start, end = 0, len(nums) - 1
        #rightmost
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        if nums[end] == target:
            ans[1] = end
        
        elif nums[start] == target:
            ans[1] = start
            
        return ans