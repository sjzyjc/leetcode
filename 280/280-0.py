class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        self.quickSelect(nums, len(nums) >> 1, 0, len(nums) - 1)
        i = 1
        offset = (len(nums)) >> 1
        print(nums)
        total = 0
        if len(nums) % 2 == 0:
            total = len(nums) - 1
        else:
            total = len(nums)
            
        while i <= (len(nums) -1) >> 1:
            nums[i], nums[total - i] = nums[total - i], nums[i]
            i += 2
        
    def quickSelect(self, nums, index, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
                
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if index <= right:
            self.quickSelect(nums, index, start, right)
        
        if index >= left:
            self.quickSelect(nums, index, left, end)
        
        
        
        
        