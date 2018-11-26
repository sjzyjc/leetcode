class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        #previous gain
        take = 0
        not_take = 0
        
        ans = 0
        for num in nums:
            ans = max(num + take, not_take)
            take = not_take
            not_take = ans
                
        return ans
        
        