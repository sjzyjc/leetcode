from collections import defaultdict
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        
        i = j = 0
        p_count = defaultdict(int)
        for char in p:
            p_count[char] += 1
        
        match_count = 0
        window_count = defaultdict(int)
        ans = []
        
        while j < len(s):
            char = s[j]
            
            if char not in p_count:
                j += 1
                i = j
                match_count = 0
                window_count = defaultdict(int)
                continue

            window_count[char] += 1
            if window_count[char] == p_count[char]:
                match_count += 1
                
            while window_count[char] > p_count[char]:
                window_count[s[i]] -= 1
                if window_count[s[i]] == p_count[s[i]] - 1:
                    match_count -= 1
                    
                i += 1
            
            if match_count == len(p_count):
                ans.append(i)
            
            j += 1
         
        return ans
                
            
        