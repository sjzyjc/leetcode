import math
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 1:
            return []
        
        ans = []
        self.helper(n, 2, [], ans)
        return ans
    
    def helper(self, remain, start, carry, ans):
        if len(carry) != 0:
            tmp = carry + []
            tmp.append(remain)
            ans.append(tmp)
        
        for i in range(start, int(math.sqrt(remain)) + 1):
            if remain % i != 0:
                continue
                
            carry.append(i)
            self.helper(remain // i, i, carry, ans)
            carry.pop()
            
        