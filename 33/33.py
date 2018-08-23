class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        smallest_index = self.findSmallest(nums)

        if target > nums[len(nums) - 1]:
            end = smallest_index - 1
            if end == -1:
                return -1
        else:
            start = smallest_index

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1    

        return -1   

    def findSmallest(self, nums):
        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[len(nums) - 1]:
                end = mid
            else:
                start = mid + 1
        return start