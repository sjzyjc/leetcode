class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        T: N * M  S: log(N * M)
        """
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        width, height = len(grid[0]), len(grid)
        counter = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    self.removeIsland(grid, i, j)
                    for k in range(len(grid)):
                        print(grid[k])
                    counter += 1

        return counter


    def removeIsland(self, grid, i, j):
        if not (0<= i < len(grid) and 0 <= j < len(grid[0])):
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.removeIsland(grid, i+1, j)
        self.removeIsland(grid, i-1, j)
        self.removeIsland(grid, i, j+1)
        self.removeIsland(grid, i, j-1) 

sl = Solution()
print(sl.numIslands([['1', '1', '1', '1', '0'], 
                     ['1', '1', '0', '1', '0'],
                     ['1', '1', '0', '0', '1']]))