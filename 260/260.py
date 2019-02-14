class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []
        
        xor = 0
        for num in nums:
            xor ^= num
        
        if xor == 0:
            return []
        
        shift = 0
        while shift < 32:
            if (xor >> shift) & 1 == 1:
                break
                
            shift += 1
            
        group_0 = group_1 = 0
        for num in nums:
            if (num >> shift) & 1 == 1:
                group_1 ^= num
            else:
                group_0 ^= num
                
        return [group_0, group_1]
                
                