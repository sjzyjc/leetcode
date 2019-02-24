class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        start = 1
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            if self.count(nums, mid) <= mid:
                start = mid + 1
            else:
                end = mid
                
        return start
    
    def count(self, nums, target):
        ret = 0
        for num in nums:
            if num <= target:
                ret += 1
                
        return ret