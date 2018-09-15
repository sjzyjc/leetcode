class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        self.ans = []
        self.helper(nums, [])
        return self.ans
    
    def helper(self, nums, carry):
        self.ans.append(carry + [])
        
        if carry and len(carry) == len(nums):
            return
        
        for num in nums:
            if not carry or num > carry[-1]:
                carry.append(num)
                self.helper(nums, carry)
                carry.remove(num)