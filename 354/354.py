class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    n^2
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        
        if not envelopes: 
            return 0
            
        for envelope in envelopes:
            envelope[1] = - envelope[1]
            
        envelopes.sort()
        f = [1 for _ in range(len(envelopes))]
        #find longest decreasing sub
        ans = 1
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] > envelopes[i][1]:
                    f[i] = max(f[i], f[j] + 1)
            
            ans = max(ans, f[i])
        
        return ans
            
        
        
