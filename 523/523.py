class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        
        mod_map = {}
        mod_map[0] = -1
        
        prefix_sum = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            if k!= 0:
                mod_val = prefix_sum % k
            else:
                mod_val = prefix_sum
                
            if mod_val in mod_map and index - mod_map[mod_val] > 1 :
                return True
            
            if mod_val not in mod_map:
                mod_map[mod_val] = index
            
        return False
        