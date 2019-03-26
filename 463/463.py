DIRS = [[0, -1], [-1, 0]]
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0] is None:
            return 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 1:
                    continue
                    
                remain = 4
                for dirr in DIRS:
                    new_i = i + dirr[0]
                    new_j = j + dirr[1]
                    if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0])):
                        continue
                        
                    if grid[new_i][new_j] != 1:
                        continue
                        
                    ans -= 1
                    remain -= 1
                
                ans += remain
                
        return ans