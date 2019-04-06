from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        idx_map = defaultdict(int)
        prefix_sum = 0
        idx_map[0] = -1
        
        ans = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            
            if target in idx_map:
                ans = max(index - idx_map[target], ans)
                
            if prefix_sum not in idx_map:
                idx_map[prefix_sum] = index
                
        
        return ans