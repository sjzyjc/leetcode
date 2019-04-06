class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length_map = {}
        ans = 1
        
        for num in nums:
            if num in length_map:
                continue
                
            left = length_map[num - 1] if num - 1 in length_map else 0
            right = length_map[num + 1] if num + 1 in length_map else 0
            
            total_len = left + right + 1
            ans = max(ans, total_len)
            #print(num, total_len)
            
            length_map[num] = total_len
            length_map[num + right] = total_len
            length_map[num - left] = total_len
            
            
        return ans
            
        