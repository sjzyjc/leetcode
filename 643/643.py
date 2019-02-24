class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        ans = -(1 << 31)
        for index, num in enumerate(nums):
            total += num
            if index < k - 1:
                continue
            
            if index >= k:
                total -= nums[index - k]
                
            ans = max(total, ans)
            
        return ans / k
                
            
                
            