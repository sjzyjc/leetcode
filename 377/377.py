class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        f = [0 for _ in range(target + 1)] 
        f[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    f[i] += f[i - num]
                    
        
        return f[-1]
                
                