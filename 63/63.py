class Solution:
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        
        count = [[0 for m in range(len(grid[0]))] for n in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    count[i][j] = 1
                    
                if grid[i][j] == 1:
                    count[i][j] = 0
                    continue
                    
                if j >= 1:
                    count[i][j] += count[i][j - 1]
                
                if i >= 1:
                    count[i][j] += count[i - 1][j]
                    
                    
        return count[-1][-1]