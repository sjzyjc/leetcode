class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if not A:
            return False
        
        k = 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                continue
                
            if k == 0:
                if A[i] > A[i - 1]:
                    k = 1
                else:
                    k = -1
                    
            elif (A[i] - A[i - 1]) * k < 0:
                return False
            
        return True
                
            