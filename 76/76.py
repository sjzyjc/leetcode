from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        target_count = defaultdict(int)
        window_count = defaultdict(int)
        for char in t:
            target_count[char] += 1
            
        satisfy = 0
        left = right = 0
        ans = (1 << 31) - 1
        ans_l = ans_r = -1
        while right < len(s):
            char = s[right]
            if char in target_count:
                window_count[char] += 1
                if window_count[char] == target_count[char]:
                    satisfy += 1
                    
            while satisfy == len(target_count) and left < len(s) and (s[left] not in target_count or window_count[s[left]] > target_count[s[left]]):
                window_count[s[left]] -= 1
                left += 1
                
            if satisfy == len(target_count) and right - left + 1 < ans:
                ans = min(ans, right - left + 1)
                ans_l = left
                ans_r = right
                
            right += 1
         
        #print(ans_l, ans_r)
        return s[ans_l:ans_r + 1] if ans_l != -1 else ""
             
            
            