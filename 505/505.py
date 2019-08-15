from collections import deque

OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1
        
        visited = {}
        queue = deque([(start[0], start[1], 0)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            if (x, y) in visited and visited[(x, y)] <= distance:
                continue
            
            visited[(x, y)] = distance
            for offset in OFFSETS:
                tmp_x = x
                tmp_y = y
                step = 0
                while (0 <= tmp_x + offset[0] < len(maze) and 0 <= tmp_y + offset[1] < len(maze[0]) and maze[tmp_x + offset[0]][tmp_y + offset[1]] == 0):
                    tmp_x += offset[0]
                    tmp_y += offset[1]
                    step += 1
                    
                queue.append((tmp_x, tmp_y, distance + step))
                
        return visited[(destination[0], destination[1])] if (destination[0], destination[1]) in visited else -1
            
        