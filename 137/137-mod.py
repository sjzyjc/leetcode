class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = 0
        for shift in range(32):
            tmp = 0
            for num in nums:
                tmp += (num >> shift) & 1
            
            
            tmp %= 3
            if shift != 31:
                ans += (tmp << shift)
            elif tmp:
                ans -= (1 << 31)
            
        return ans
                
                
        