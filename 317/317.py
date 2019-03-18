from collections import deque
INT_MAX = (1 << 31) - 1
OFFSETS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        building_count = 0
        reach_count = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        distance = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 1:
                    continue
                    
                building_count += 1
                self.bfs(grid, i, j, reach_count, distance)
        
        ans = INT_MAX
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 or reach_count[i][j] < building_count:
                    continue
                    
                ans = min(ans, distance[i][j])
                
        #print(distance, reach_count)
        return ans if ans < INT_MAX else -1
    
    def bfs(self, grid, i, j, reach_count, distance):
        queue = deque([])
        visited = set()
        
        for offset in OFFSETS:
            queue.append((i + offset[0], j + offset[1], 1))
        
        while queue:
            i, j, dis = queue.popleft()
            
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or (i, j) in visited:
                continue
                
            visited.add((i, j))
            if grid[i][j] != 0:
                continue
                
            #update distance
            reach_count[i][j] += 1
            distance[i][j] += dis
                
            for offset in OFFSETS:
                new_i, new_j = i + offset[0], j + offset[1]
                queue.append((new_i, new_j, dis + 1))
                    
            
                
            
            
        
        