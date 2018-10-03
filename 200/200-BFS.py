from collections import deque
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
            for j in range(len(grid[i])):
                if self.findIsland(grid, i, j):
                    counter += 1

        return counter
        
    def findIsland(self, grid, i, j):
        queue = deque()
        queue.append((i, j))
        findIsland = False
        
        while queue:
            i_tmp, j_tmp = queue.popleft()
            
            if not (0<= i_tmp < len(grid) and 0<= j_tmp < len(grid[0])):
                continue
            
            if grid[i_tmp][j_tmp] == 0:
                continue
            
            findIsland = True
            grid[i_tmp][j_tmp] = 0
            offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for offset in offsets:
                queue.append((i_tmp + offset[0] , j_tmp + offset[1]))
        
        return findIsland      