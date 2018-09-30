class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        f = [[(1 << 31) - 1 for j in range(len(grid[0]))] for i in range(2)]
        prev, cur = 1, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    f[i][j] = grid[0][0]
                    continue
                
                min_prev = (1 << 31) - 1
                if i > 0:
                    min_prev = min(f[prev][j], min_prev)
        
                if j > 0:
                    min_prev = min(f[cur][j - 1], min_prev)
                
                f[cur][j] = min_prev + grid[i][j]
            
            prev, cur = cur, prev
                
        return f[prev][-1]
                
