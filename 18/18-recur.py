class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        self.findNSum(nums, target, 4, [], ret)
        return ret
    
    def findNSum(self, nums, target, N, prev, ret):
        if not nums or len(nums) < N or N == 1:
            return 
        if N == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ret.append(prev + [nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - N + 1):
                if nums[i] * N > target or nums[-1] * N < target:
                    return
                
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.findNSum(nums[i+1:], target - nums[i], N - 1, prev + [nums[i]], ret)
                    