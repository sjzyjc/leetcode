class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        
        prefix_sum = [0 for _ in range(len(nums) + 1)]

        ans = len(nums)
        for index, num in enumerate(nums):
            prefix_sum[index + 1] = prefix_sum[index] + num
            
            if prefix_sum[index + 1] < s:
                continue
                
            start, end = 0, index
            while start + 1 < end:
                mid = (start + end) // 2
                if prefix_sum[index + 1] - prefix_sum[mid] >= s:
                    start = mid
                else:
                    end = mid - 1
                    
            if prefix_sum[index + 1] - prefix_sum[end] >= s:
                ans = min(ans, index + 1 - end)
            else:
                ans = min(ans, index + 1 - start)
                
        return ans
                
            
            