class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        ans = (1 << 31) - 1
        if nums[start] == nums[end]:
            ans = min(ans, nums[end])
            while start <= end and nums[start] == nums[-1]:
                start += 1
                
            while start <= end and nums[end] == nums[-1]:
                end -= 1
                
        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid + 1
                
        if start < len(nums):
            ans = min(ans, nums[start])
            
        return ans
            