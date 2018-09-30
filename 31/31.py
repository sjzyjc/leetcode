class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        first = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                first = i - 1
                break
        
        if first is None:
            self.swap(nums, 0, len(nums) - 1)
            return
        
        second = None
        for j in range(len(nums) - 1, first, -1):
            if nums[j] > nums[first]:
                second = j
                break
        
        nums[first], nums[second] = nums[second], nums[first]
        self.swap(nums, first + 1, len(nums) - 1)

    
    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1