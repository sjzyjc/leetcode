from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S or not T:
            return T
        
        t_count = defaultdict(int)
        for char in T:
            t_count[char] += 1
        
        ans = []
        for char in S:
            if char not in t_count:
                continue
                
            ans.extend([char] * t_count[char])
            del t_count[char]
            
        for i in t_count:
            ans.extend([i] * t_count[i])
            
        return "".join(ans)
    