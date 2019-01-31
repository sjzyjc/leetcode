from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        left = right = 0
        window_count = defaultdict(int)
        #count for chars that has >=1 ocurrence
        count = 0
        
        ans = 0
        while right < len(s):
            charr = s[right]
            
            if window_count[charr] == 0:
                count += 1
            window_count[charr] += 1
            
            if count <= 2:
                ans = max(ans, right - left + 1)
                
            while count > 2 and window_count[s[left]] > 0:
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    count -= 1
                left += 1
                
            right += 1
            
        return ans
            
            
            
            
        
        