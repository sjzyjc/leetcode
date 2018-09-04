class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        left, right = 0, len(nums) - 1
        for current in nums:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]    
                right -= 1 
                

        print(nums)       

sl = Solution()
print(sl.sortColors([2,2,2,2,2]))