class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        
        start = min(nums)
        end = max(nums)
        
        while start + 1e-5 < end:
            mid = (start + end) / 2

            if self.canFind(nums, k, mid):
                start = mid
            else:
                end = mid
                
        return start
    
    def canFind(self, nums, k, avg):
        rightSum = leftSum = minLeftSum = 0
        
        for index, num in enumerate(nums):
            rightSum += (num - avg)
                
            if index >= k:
                leftSum += (nums[index - k] - avg)
                minLeftSum  = min(minLeftSum, leftSum)
            
            if index >= k - 1:
                if rightSum - minLeftSum >= 0:
                    return True
                
        return False
                
        