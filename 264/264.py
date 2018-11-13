class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        
        f = [-1 for i in range(n)]
        f[0] = 1
        ptr1, ptr2, ptr3 = 0, 0, 0
    
        min_val = (1 << 31) - 1
        
        for i in range(1, n):
            f[i] = min(2 * f[ptr1], 3 * f[ptr2], 5 * f[ptr3])
            
            if 2 * f[ptr1] == f[i]:
                ptr1 += 1
                
            if 3 * f[ptr2] == f[i]:
                ptr2 += 1
                
            if 5 * f[ptr3] == f[i]:
                ptr3 += 1
                
        return f[-1]
                
    
                
            
        