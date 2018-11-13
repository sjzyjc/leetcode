class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        left, right, current = 0, len(nums) - 1, 0
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[right] = nums[right], nums[current]    
                right -= 1 