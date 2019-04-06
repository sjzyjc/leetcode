class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count_1s = [0 for _ in range(32)]
        for num in nums:
            for shift in range(32):
                count_1s[shift] += (num >> shift) & 1
        
        total = len(nums)
        ans = 0
        for count in count_1s:
            ans += count * (total - count)
            
        return ans