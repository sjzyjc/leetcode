class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        hashmap = {}
        hashmap[0] = 1
        return self.helper(n, hashmap)
    
    def helper(self, n, hashmap):
        if n in hashmap:
            return hashmap[n]
        
        count = 0
        if n >= 1:
            count += self.helper(n-1, hashmap)
        
        if n >= 2:
            count += self.helper(n-2, hashmap)
            
        hashmap[n] = count
        return count
            
        
        
        