from collections import deque

OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def shortestDistance(self, maze, start, destination):
        if not maze or not maze[0]:
            return -1
        
        visited = set()
        queue = deque([(start[0], start[1], 0)])
        
        while queue:
            print(queue)
            x, y, distance = queue.popleft()
            
            if (x, y) in visited:
                continue
                
            if destination[0] == x and destination[1] == y:
                return distance
            
            visited.add((x, y))
            for offset in OFFSETS:
                tmp_x = x
                tmp_y = y
                step = 0
                while not (0 <= tmp_x + offset[0] < len(maze) and 0 <= tmp_y + offset[1] < len(maze[0]) and maze[tmp_x + offset[0]][tmp_y + offset[1]] == 0):
                    tmp_x += offset[0]
                    tmp_y += offset[1]
                    step += 1
                    
                queue.append((tmp_x, tmp_y, distance + step))
                
        return -1
            
sl = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
dest = [4,4]
print(sl.shortestDistance(maze, start, dest))