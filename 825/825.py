class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return []
        
        count = [0 for _ in range(121)]
        for age in ages:
            count[age] += 1
            
        ps = [0 for _ in range(len(count))]
        for index, num in enumerate(count):
            ps[index] = ps[index - 1] + num
            
        ans = 0
        #print(count, ps)
        for age in ages:
            upper_bound = age
            lower_bound = age // 2 + 7
                
            # lower_bound < x <= upper_bound
            if lower_bound >= upper_bound:
                continue
                
            ans += ps[upper_bound] - ps[lower_bound] - 1
            
        return ans
            
                
            
            
            
                
            
            
        
        