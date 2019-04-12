from collections import deque
import heapq

OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1
        
        visited = set()
        heap = [(0, start[0], start[1])]
        weight = [[(1 << 31) - 1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        
        while heap:
            w, x, y = heapq.heappop(heap)
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            for offset in OFFSETS:
                tmp_x = x
                tmp_y = y
                step = 0
                while (0 <= tmp_x + offset[0] < len(maze) and 0 <= tmp_y + offset[1] < len(maze[0]) and maze[tmp_x + offset[0]][tmp_y + offset[1]] == 0):
                    tmp_x += offset[0]
                    tmp_y += offset[1]
                    step += 1
                    
                if (tmp_x, tmp_y) not in visited and w + step < weight[tmp_x][tmp_y]:
                    weight[tmp_x][tmp_y] = w + step
                    heapq.heappush(heap, (weight[tmp_x][tmp_y], tmp_x, tmp_y))
                    
            
        ans = weight[destination[0]][destination[1]]
        return ans if ans != (1 << 31) - 1 else -1