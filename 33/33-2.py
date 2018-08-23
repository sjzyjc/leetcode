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

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
           
            if nums[mid] > nums[end]:
                if target > nums[end] and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:    
                if target <= nums[end] and target > nums[mid]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1    