class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start < end:
            mid =  start + (end - start) // 2
            
            if nums[mid] > nums[len(nums) - 1]:
                start = mid + 1
            else:
                end = mid
             
        return nums[start]
                