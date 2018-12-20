class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        self.ans = (1 << 31) - 1
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.dfs(grid, 0, 0, grid[0][0], visited)
        return self.ans
    
    def dfs(self, grid, i, j, max_val, visited):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or visited[i][j]:
            return

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            max_val = max(max_val, grid[i][j])
            self.ans = min(self.ans, max_val)
            return
        
        visited[i][j] = True
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for offset in offsets:
            self.dfs(grid, i + offset[0], j + offset[1], max(max_val, grid[i][j]), visited)
            
        visited[i][j] = False
        
sl = Solution()
print(sl.swimInWater([[22,4,21,12,11],[1,10,23,17,5],[14,7,2,9,16],[3,15,20,0,18],[8,24,13,19,6]]))