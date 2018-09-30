class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target is None:
            return []
        
        ans = []
        candidates.sort()
        self.helper(candidates, 0, target, [], ans)
        return ans
    
    def helper(self, nums, start_index, remain, carry, ans):
        if remain == 0:
            ans.append(carry + [])
            return
        
        for i in range(start_index, len(nums)):
            if nums[i] > remain:
                break
            carry.append(nums[i])
            self.helper(nums, i, remain - nums[i], carry, ans)
            carry.remove(nums[i])
        