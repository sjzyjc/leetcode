class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
            
        if nums is None or len(nums) == 0:
            return 0
        
        nums.sort()
        left = 0

        for right in range(len(nums)):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1                
        
        return left + 1

sl = Solution()
print(sl.deduplication([1,3,1,4,4,2]))       