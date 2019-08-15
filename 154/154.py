class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        
        start, end =  0, len(nums) -1
        last_num = nums[-1]
        
        #[1, 1, 1, 0, 1, 1]
        if nums[0] == nums[-1]:
            while start < end and nums[start] == nums[-1]:
                start += 1
                
            while start < end and nums[end] == nums[-1]:
                end -= 1
        
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] <= last_num:
                end = mid
            else: 
                start = mid + 1    

        return min(nums[start], last_num)