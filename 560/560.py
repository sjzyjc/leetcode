from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if not nums:
            return -1
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        tmp = 0
        count = 0
        for num in nums:
            tmp += num
            if tmp - k in prefix_sum:
                count += prefix_sum[tmp - k]
                
            prefix_sum[tmp] += 1
            
        return count