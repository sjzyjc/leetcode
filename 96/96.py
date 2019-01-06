class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        
        return self.helper(1, n)
    
    def helper(self, start, end):
        if start >= end:
            return 1
        
        ans = 0
        for i in range(start, end + 1):
            #print(i)
            ans += self.helper(start, i - 1) * self.helper(i + 1, end)
            
        return ans

sl = Solution()
print(sl.numTrees(19))