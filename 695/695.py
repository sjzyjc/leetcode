class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        height, width = len(grid), len(grid[0])
        maxium = 0
        for i in range(height):
            for j in range(width):
                size =  self.findIslandSize(grid, i, j)
                if size > maxium:
                    maxium = size

        return maxium

    def findIslandSize(self, grid, i ,j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return 0

        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        return self.findIslandSize(grid, i+1, j) + self.findIslandSize(grid, i-1, j) + self.findIslandSize(grid, i, j+1) + self.findIslandSize(grid, i, j-1) + 1

            
        
sl = Solution()
print(sl.maxAreaOfIsland([['1', '1', '0', '0', '0'], 
                          ['1', '1', '0', '0', '0'],
                          ['0', '0', '0', '1', '1'],
                          ['0', '0', '0', '1', '1']]))