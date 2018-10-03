class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        c_index = len(nums) - 1
        ret = nums[len(nums) - 1] + nums[len(nums) - 2] + nums[0]
        
        while c_index >= 0:
            left, right = 0, c_index - 1
            while left < right:
                total = nums[left] + nums[right] + nums[c_index]
                if abs(total - target) <= abs(ret - target):
                    ret = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1
            c_index -= 1
            
        return ret
            
            
                    
                    