class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        f = [(1 << 31) - 1 for _ in range(len(nums) + 1)]
        f[0] = - (1 << 31)
        last_update = 0
        
        for index in range(len(nums)):
            start, end = 0, index
            target = nums[index]
            #find last smallest 
            while start + 1 < end:
                mid = start + (end - start) // 2
                if f[mid] < target:
                    start = mid
                else:
                    end = mid - 1
                    
            last = 0
            if f[end] < nums[index]:
                last  = end + 1
            else:
                last = start + 1
            
            f[last] = target
            last_update = max(last, last_update)

        return last_update
            
        