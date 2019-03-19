class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        best case: logN
        worst case: N
        """
        if not nums:
            return False
        
        if target == nums[-1]:
            return True
        
        start = 0
        end = len(nums) - 1
        if nums[start] == nums[end]:
            while start <= end and nums[start] == nums[-1]:
                start += 1
                
            while start <= end and nums[end] == nums[-1]:
                end -= 1
        
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[-1]:
                if target > nums[-1] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[-1] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False