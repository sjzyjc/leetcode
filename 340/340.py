from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k < 0 or not s:
            return 0
        
        left = right = 0
        
        hash_map = defaultdict(int)
        ans = 0
        while right < len(s):
            charr = s[right]
            hash_map[charr] += 1
            
            while len(hash_map) > k:
                hash_map[s[left]] -= 1
                
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                    
                left += 1
                
            if len(hash_map) <= k:
                ans = max(ans, right - left + 1)
                
            right += 1
            
        return ans