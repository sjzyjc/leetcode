class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        values = []
        for col in grid:
            for val in col:
                values.append(val)
        
        values.sort()
        start, end = 0, len(values) - 1
        while start < end:
            mid = start + (end - start) // 2
            
            visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
            if self.canPass(grid, values[mid], 0, 0, visited):
                end = mid
            else:
                start = mid + 1
        
        return start
                
    
    def canPass(self, grid, time, i, j, visited):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or visited[i][j] or grid[i][j] > time:
            return False
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        
        visited[i][j] = True
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = False
        for offset in offsets:
            result = result or self.canPass(grid, time, i + offset[0], j + offset[1], visited)
            
        return result
        
        