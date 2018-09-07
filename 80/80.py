class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0 
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num                
                i += 1
                
        return  i             
                
            