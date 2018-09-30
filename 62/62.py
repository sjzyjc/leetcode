class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        M*N
        """
        if m <= 0 or n <= 0:
            return 0
        
        f = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    f[0][0] = 1
                
                if i > 0:
                    f[i][j] += f[i - 1][j]
                    
                if j > 0:
                    f[i][j] += f[i][j - 1]
                    
                    
        return f[n - 1][m - 1]