from collections import defaultdict
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return []
        
        ages.sort()
        count = defaultdict(int)
        for age in ages:
            count[age] += 1
        
        i = j = ans = 0
        while j < len(ages):
            if j + 1 < len(ages) and ages[j] == ages[j + 1]:
                j += 1
                continue
                
            while i < j and ages[i] <= 0.5 * ages[j] + 7:
                i += 1
                
            if i < j:
                ans += (j - i) * count[ages[j]]
                
            j += 1
            
        return ans