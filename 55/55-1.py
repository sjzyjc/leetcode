class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        
        maximum = 0
        for index, num in enumerate(nums):
            if index > maximum:
                break
                
            maximum = max(maximum, index + num)
            
        return len(nums) - 1 <= maximum