class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None
            
        self.quickSort(nums, len(nums) - k, 0, len(nums) -1)
        return nums[len(nums) - k]
        
    def quickSort(self, nums, index, start, end):
        if start >= end:
            return

        pivot = nums[(start + end) // 2]

        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if index >= left:
            self.quickSort(nums, index, left, end)
        
        if index <= right:
            self.quickSort(nums, index, start, right)
            
        
              