class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):        
        if not grid or not grid[0]:
            return 0
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.findIsland(grid, i, j):
                    counter += 1
                
        return counter
        
        
    def findIsland(self, grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return False
        
        if grid[i][j] == 0:
            return False
        
        grid[i][j] = 0
        self.findIsland(grid, i + 1, j)  
        self.findIsland(grid, i - 1, j)  
        self.findIsland(grid, i, j + 1)  
        self.findIsland(grid, i, j - 1)
        
        return True