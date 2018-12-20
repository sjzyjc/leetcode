class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        for envelope in envelopes:
            envelope[1] = -envelope[1]
        
        envelopes.sort()
        #find longest decreasing subsequence
        print(envelopes)
        f = [-(1 << 31) for _ in range(len(envelopes) + 1)]
        f[0] = (1 << 31) - 1
        
        ans = 0
        for index in range(len(envelopes)):
            start, end = 0, index
            target = envelopes[index][1]
            while start + 1 < end:
                mid = start + (end - start) // 2
                if f[mid] > target:
                    start = mid
                else:
                    end = mid - 1
                    
            to_update = 0
            if f[end] > target:
                to_update = end + 1
            else:
                to_update = start + 1
            
            f[to_update] = target
            ans = max(ans, to_update)
            
        return ans
                    
                    
                    