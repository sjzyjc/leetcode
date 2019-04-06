DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0] or not start or not destination:
            return False
        
        queue = deque([(start[0], start[1])])
        visited = set()
        
        while queue:
            x, y = queue.popleft()
            
            if x == destination[0] and y == destination[1]:
                return True
            
            if (x, y) in visited:
                continue
            
            #print(x, y)
            visited.add((x, y))
            for direction in DIR:
                new_x = x
                new_y = y
                while (0 <= new_x + direction[0] < len(maze) and 0 <= new_y + direction[1] < len(maze[0])) and maze[new_x + direction[0]][new_y + direction[1]] == 0:
                    new_x += direction[0]
                    new_y += direction[1]
                    
                queue.append((new_x, new_y))
                
        return False
            