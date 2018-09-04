class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end =  mid - 1
        
        return -1