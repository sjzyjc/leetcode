class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target is None:
            return None
        
        ans = []
        candidates.sort()
        self.helper(candidates, target, 0, [], ans)
        
        return ans
    
    def helper(self, nums, remain, start_index, carry, ans):
        if remain == 0:
            ans.append(carry + [])
            return
        
        for i in range(start_index, len(nums)):
            if nums[i] > remain:
                break
            
            if i > 0 and nums[i - 1] == nums[i] and i > start_index:
                continue
                
            carry.append(nums[i])
            self.helper(nums, remain - nums[i], i + 1, carry, ans)
            carry.remove(nums[i])