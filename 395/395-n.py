from collections import defaultdict
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        O(N)
        """
        if not s or not k:
            return 0
        
        ans = 0
        for i in range(1, len(set(s)) + 1):
            ans = max(ans, self.findMaxUniq(s, k, i))
            print(i, ans)
            
        return ans
    
    def findMaxUniq(self, s, k, n):
        i = j = 0
        no_uniq = no_le = 0
        window_count = defaultdict(int)
        
        ans = 0
        while j < len(s):
            char = s[j]
            
            if window_count[char] == 0:
                no_uniq += 1
                
            window_count[char] += 1
            if window_count[char] == k:
                no_le += 1
            
            if no_uniq == no_le:
                ans = max(ans, j - i + 1)
                
            while no_uniq > n:
                window_count[s[i]] -= 1
                if window_count[s[i]] == 0:
                    no_uniq -= 1
                    
                if window_count[s[i]] == k - 1:
                    no_le -= 1
                    
                i += 1
            
            j += 1
            
        return ans
            
            
        
        
        
            