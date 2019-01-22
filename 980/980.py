OFFSETS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        count = 0
        start_i = start_j = end_i = end_j = -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == 0:
                    count += 1
        
        self.counter = 0
        self.dfs(grid, start_i, start_j, count)
        return self.counter
    
    def dfs(self, grid, cur_i, cur_j, remain):
        if not (0 <= cur_i < len(grid) and  0 <= cur_j < len(grid[0])):
            return
        
        if grid[cur_i][cur_j] == 2 and remain == 0:
            self.counter += 1
            return
        
        if grid[cur_i][cur_j] == -1:
            return
        
        orig = grid[cur_i][cur_j]
        if orig == 0:
            remain -= 1
            
        grid[cur_i][cur_j] = -1
        for offset in OFFSETS:
            self.dfs(grid, cur_i + offset[0], cur_j + offset[1], remain)
        
        #backtrack
        if orig == 0:
            remain += 1
        grid[cur_i][cur_j] = orig 
        