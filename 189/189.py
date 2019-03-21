class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return 
        
        def reverse(start, end):
            left = start
            right = end
            while left < right: 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        k = k % len(nums)
        reverse(0, len(nums) - k - 1)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums) - 1)
        
        