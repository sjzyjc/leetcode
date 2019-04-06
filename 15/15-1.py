class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        
        ans = []
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
                
            val = nums[index]
            target = 0 - val
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    ans.append([val, nums[i], nums[j]])
                    
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                        
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
                        
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
                    
        return ans