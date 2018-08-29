class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexMap = {}
        for i in range(len(nums)):
            if target - nums[i] in indexMap:
                return [indexMap[target - nums[i]], i]

            indexMap[nums[i]] = i

sl = Solution()
print(sl.twoSum([5],10))