class Solution:
    def longestLine(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        
        f = [[[0 for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(2)]
        pre, cur = 1, 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):    
                if grid[i][j] == 0:
                    for k in range(4):
                        f[cur][j][k] = 0
                    continue
                
                f[cur][j][0] = f[cur][j - 1][0] + 1 if j > 0 else 1
                f[cur][j][1] = f[pre][j][1] + 1 if i > 0 else 1
                f[cur][j][2] = f[pre][j - 1][2] + 1 if i > 0 and j > 0 else 1
                f[cur][j][3] = f[pre][j + 1][3] + 1 if i > 0 and j < len(grid[i]) - 1 else 1
                
                ans = max(ans, f[cur][j][0], f[cur][j][1], f[cur][j][2], f[cur][j][3])  
            pre, cur = cur, pre
                
        return ans