class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        total = sum(nums)
        left_sum = 0
        for index, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return index
            left_sum += num
            
        return -1