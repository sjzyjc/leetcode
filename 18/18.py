class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        
        d_index = len(nums) - 1
        ret = []
        while d_index >= 3:
            c_index = d_index - 1
            while c_index >= 2:
                left, right = 0, c_index - 1
                while left < right:
                    total = nums[left] + nums[right] + nums[c_index] + nums[d_index]
                    if total == target:
                        ret.append([nums[left], nums[right], nums[c_index], nums[d_index]])
                        left = self.findNextUniqueAscend(nums, left)
                        right = self.findNextUniqueDecend(nums, right)

                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                    
                while c_index >=2 and nums[c_index] == nums[c_index - 1]:
                    c_index -= 1
                c_index = self.findNextUniqueDecend(nums, c_index)
            
            d_index = self.findNextUniqueDecend(nums, d_index)
            
        return ret
    
    def findNextUniqueDecend(self, nums, index):
        while index - 1 >= 0 and nums[index] == nums[index - 1]:
            index -= 1
        return index - 1
    
    def findNextUniqueAscend(self, nums, index):
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        return index + 1        
                
            