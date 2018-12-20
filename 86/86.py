class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        
        self.helper(0, n, res)
        
        return res
    
    def helper(self, orig, n, res):
        if orig in res:
            return False
        else:
            res.append(orig)
                
        for i in range(n):
            bit = (orig >> i) & 1
            if bit == 0:
                has_next = self.helper(orig + (1 << i), n, res)
            else:
                has_next = self.helper(orig - (1 << i), n, res)
                
            if has_next:
                break
                
        return True
            