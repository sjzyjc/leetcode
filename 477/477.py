class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        one_count = [0 for _ in range(32)]
        total = len(nums)
                
        for num in nums:
            i = 0
            while (num >> i) > 0:
                one_count[i] += (num >> i) & 1
                i += 1
                
        ans = 0
        for count in one_count:
            ans += count * (total - count)
            
        return ans