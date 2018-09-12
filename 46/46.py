class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.helper(nums, 0)
        return self.ans
    
    def helper(self, nums, length):
        if length == len(nums):
            self.ans.append(nums+[])
            return
        
        for i in range(length, len(nums)):
            nums[i], nums[length] = nums[length], nums[i]
            self.helper(nums, length + 1)
            nums[i], nums[length] = nums[length], nums[i]
