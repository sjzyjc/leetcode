class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        c_index = len(nums) - 1
        ret = []
        while c_index >= 0:
            
            two_sum_list = self.findTwoSum(nums[:c_index], -nums[c_index])
            for i in two_sum_list: 
                i.append(nums[c_index])
                ret.append(i)

            while c_index - 1 >= 0 and nums[c_index - 1] == nums[c_index]:
                c_index -= 1

            c_index -= 1    

        return ret

    def findTwoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        ret = []
        while left < right:
            total_sum = nums[left] + nums[right]
            if total_sum == target:
                ret.append([nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1    

            elif total_sum < target:
                left += 1
            else:
                right -= 1                                 
        return ret

sl = Solution()
print(sl.threeSum([-2,-1,0,1,2,-1,-4]))       