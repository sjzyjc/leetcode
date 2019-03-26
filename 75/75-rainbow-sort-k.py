class Solution:
    def sortColors2(self, nums, k):        
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return []

        self.quickSort(nums, 0, len(nums) - 1, 1, k)    

    def quickSort(self, nums, start, end, start_color, end_color):
        if start >= end or start_color == end_color:
            return 

        left, right = start, end
        pivot = (start_color + end_color) // 2
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.quickSort(nums, start, right, start_color, pivot)
        self.quickSort(nums, left, end, pivot + 1, end_color)        

