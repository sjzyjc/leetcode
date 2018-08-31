class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        last_non_zero = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                last_non_zero += 1
                nums[last_non_zero] = nums[i]

        for j in range(last_non_zero + 1, len(nums)):
            nums[j] = 0

sl = Solution()
print(sl.moveZeroes([1,0,2,3,0]))       

                