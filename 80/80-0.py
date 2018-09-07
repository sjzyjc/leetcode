class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i, j = 0, 1
        counter = 0
        while j < len(nums):
            if nums[j] == nums[j - 1]:
                counter += 1
                if counter < 2:
                    i += 1
                    nums[i] = nums[j]
                    
            else:
                i += 1
                nums[i] = nums[j]
                counter = 0
                
            j += 1
            
        return i + 1
                
                
            