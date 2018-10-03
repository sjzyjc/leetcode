class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        nums.sort()
        c_index = len(nums) - 1
        counter = 0
        while c_index >= 0:
            remain = target - nums[c_index]
            left, right = 0, c_index - 1

            while left < right:
                actual = nums[left] + nums[right]
                if actual < remain:
                    counter += (right - left)
                    left += 1
                else:
                    right -= 1
                    
            c_index -= 1

        return counter  