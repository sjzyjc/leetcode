class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        ans = []
        nums.sort()
        self.helper(nums, 0, [], ans)
        return ans
    
    def helper(self, nums, start_index, carry, ans):
        ans.append(carry + [])
        
        for i in range(start_index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i > start_index:
                continue
                
            carry.append(nums[i])
            self.helper(nums, i + 1, carry, ans)
            carry.pop()