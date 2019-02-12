from collections import defaultdict
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        T(nlogn)
        S(logN) worst case
        """
        if not s or not k:
            return 0
        
        return self.helper(0, len(s) - 1, s, k)
    
    def helper(self, start, end, s, k):
        if start > end or end - start + 1 < k or start < 0 or end >= len(s):
            return 0
            
        count = defaultdict(int)
        for index in range(start, end + 1):
            count[s[index]] += 1
            
        ans = 0
        prev = start
        no_break = True
        for index in range(start, end + 1):
            charr = s[index]
            if count[charr] < k:
                no_break = False
                ans = max(ans, self.helper(prev, index - 1, s, k))
                prev = index + 1
                
        if no_break:
            ans = end - start + 1
        
        if prev != start:
            ans = max(ans, self.helper(prev, end, s, k))
            
        return ans
            
        
        
        