class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        

        def sort(left, right, target):
            while left < right:
                while left < right and nums[left] < target:
                    left += 1
                
                while left < right and nums[right] >= target:
                    right -= 1
                    
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                    
        sort(0, len(nums) - 1, 2)
        #print(nums)
        sort(0, len(nums) - 1, 1)