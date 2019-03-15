class Solution:
    def canPartitionKSubsets(self, nums, k) -> bool:
        if not nums or k <= 0:
            return False
        
        remain_map = {}
        size = sum(nums) // k
        for num in nums:
            if num > size:
                return False
            
        for i in range(k):
            remain_map[i] = size
            
        return self.helper(nums, 0, remain_map, 0)
    
    def helper(self, nums, start_index, remain_map, satisfy):
        if satisfy == len(remain_map) and start_index == len(nums):
            return True
        
        num = nums[start_index]
        for i in remain_map:
            if num <= remain_map[i]:
                remain_map[i] -= num
                if remain_map[i] == 0:
                    satisfy += 1
                if self.helper(nums, start_index + 1, remain_map, satisfy):
                    return True
                #backtrack
                remain_map[i] += num
                if remain_map[i] == num:
                    satisfy -= 1
        
        return False
                
test = [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037]
sl = Solution()
print(sl.canPartitionKSubsets(test, 4))       