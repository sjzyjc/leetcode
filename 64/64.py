class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        f = [[(1 << 31) - 1 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    f[i][j] = grid[0][0]
                    continue
                
                min_prev = (1 << 31) - 1
                if i > 0:
                    min_prev = min(f[i - 1][j], min_prev)
        
                if j > 0:
                    min_prev = min(f[i][j - 1], min_prev)
                
                f[i][j] = min_prev + grid[i][j]
                
        return f[-1][-1]
                
