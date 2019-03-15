class Solution:
    def canPartitionKSubsets(self, nums, k):
        if not nums or k <= 0:
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False

        size = total // k
        nums.sort()
        for ptr in range(len(nums) - 1, -1, -1):
            num = nums[ptr]
            if num > size:
                return False
            if num == size:
                k -= 1

            if num < size:
                break

        remain_map = [0 for _ in range(k)]
        return self.helper(nums, ptr, remain_map, 0, size)
    
    def helper(self, nums, start_index, remain_map, satisfy, size):
        if satisfy == len(remain_map) and start_index == -1:
            return True
        
        num = nums[start_index]
        for i in range(len(remain_map)):
            if num + remain_map[i] <= size:
                remain_map[i] += num
                if remain_map[i] == size:
                    satisfy += 1
                if self.helper(nums, start_index - 1, remain_map, satisfy, size):
                    return True
                #backtrack
                if remain_map[i] == size:
                    satisfy -= 1
                remain_map[i] -= num

            if remain_map[i] == 0:
                break
        
        return False
                
        
test = [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037]
sl = Solution()
print(sl.canPartitionKSubsets(test, 4))