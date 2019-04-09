from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        
        if not s:
            return True
        
        if not t:
            return False
        
        if len(s) > len(t):
            return False
        
        index_map = defaultdict(list)
        for index, charr in enumerate(t):
            index_map[charr].append(index)
        
        last_index = -1
        for charr in s:
            last_index = self.findNext(index_map[charr], last_index)
            #print(last_index)
            if last_index < 0:
                return False
            
        return True
    
    def findNext(self, nums, target):
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
                
        if nums[start] > target:
            return nums[start]
        
        return -1