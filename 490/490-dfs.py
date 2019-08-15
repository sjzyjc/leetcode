DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0] or not start or not destination:
            return False
        
        return self.dfs(maze, (start[0], start[1]), (destination[0], destination[1]), set())
    
    def dfs(self, maze, cur, destination, visited):
        if cur == destination:
            return True
        
        if cur in visited:
            return False
        
        visited.add(cur)
        ans = False
        for direction in DIR:
            new_x = cur[0]
            new_y = cur[1]
            
            while (0 <= new_x + direction[0] < len(maze) and 0 <= new_y + direction[1] < len(maze[0])) and maze[new_x + direction[0]][new_y + direction[1]] == 0:
                new_x += direction[0]
                new_y += direction[1]
                    
            if self.dfs(maze, (new_x, new_y), destination, visited):
                ans = True
                break
                
        return ans
                
                
        
        