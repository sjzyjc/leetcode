class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        x_arr = []
        y_arr = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x_arr.append(i)
        
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    y_arr.append(j)
                    
        x = x_arr[len(x_arr) // 2]
        y = y_arr[len(y_arr) // 2]
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += abs(x - i) + abs(y - j)
                
        return ans
                
        