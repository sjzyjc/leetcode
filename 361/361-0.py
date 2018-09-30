class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        height = len(grid)
        width = len(grid[0])
        
        up = [[0 for i in range(width)] for j in range(height)]
        down = [[0 for i in range(width)] for j in range(height)]
        left = [[0 for i in range(width)] for j in range(height)]
        right = [[0 for i in range(width)] for j in range(height)]
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] ==  "W":
                    up[i][j] = 0
                    left[i][j] = 0
                    continue
                    
                if grid[i][j] == "E":
                    up[i][j] += 1
                    left[i][j] += 1
                    
                if i > 0:
                    up[i][j] += up[i - 1][j]
                
                if j > 0:
                    left[i][j] += left[i][j - 1]
                    
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if grid[i][j] == "W":
                    down[i][j] = 0
                    right[i][j] = 0
                    continue
                    
                if grid[i][j] == "E":
                    down[i][j] += 1
                    right[i][j] += 1
                
                if i < len(grid) - 1:
                    down[i][j] += down[i + 1][j]
                
                if j < len(grid[0]) - 1:
                    right[i][j] += right[i][j + 1]
                    
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] != "0":
                    continue
                    
                count = up[i][j] + down[i][j] + left[i][j] + right[i][j]
                if count > ans:
                    ans = count
                    
        return ans