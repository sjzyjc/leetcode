INT_MAX = (1 << 31)
INT_MIN = -(1 << 31) - 1
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        #small to large
        large = [INT_MIN for _ in range(3)]
        small = [INT_MAX for _ in range(2)]
        
        for num in nums:
            if num >= large[2]:
                large[2], large[1], large[0] = num, large[2], large[1]
            elif num >= large[1]:
                large[1], large[0] = num, large[1]
            elif num > large[0]:
                large[0] = num
                
            
            if num <= small[0]:
                small[0], small[1] = num, small[0]
            elif num < small[1]:
                small[1] = num
                
        
        return max(small[0] * small[1] * large[-1], large[0] * large[1] * large[2])
        