class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        
        prev_sum = 0
        max_sum = -(1 << 31)
        min_sum = (1 << 31) - 1
        min_ps = max_ps = 0
        
        
        for index, num in enumerate(A):
            cur_sum = prev_sum + num
            max_sum = max(max_sum, cur_sum - min_ps)
            min_ps = min(cur_sum, min_ps)
            
            min_sum = min(min_sum, cur_sum - max_ps)
            max_ps = max(cur_sum, max_ps)
            
            prev_sum = cur_sum
            
        if cur_sum == min_sum:
            return max_sum
        
        return max(max_sum, cur_sum - min_sum)
        