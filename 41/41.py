class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        for index in range(len(nums)):
            while nums[index] > 0 and nums[index] <= len(nums) and nums[index] != nums[nums[index] - 1]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                
                
        for index, num in enumerate(nums):
            if index + 1 != num:
                return index + 1
            
        return len(nums) + 1
            
                
            
            
        
                
        