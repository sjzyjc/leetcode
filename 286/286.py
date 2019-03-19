from collections import deque

OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return 
        
        queue = deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    queue.append((i,j, 0))
        
        visited = set()
        while queue:
            i, j, distance = queue.popleft()
            
            if not (0 <= i < len(rooms) and 0 <= j < len(rooms[0])):
                continue
                
            if rooms[i][j] == -1:
                continue
            
            if (i, j) in visited:
                continue
                
            visited.add((i, j))
            if rooms[i][j] != 0:
                rooms[i][j] = distance
                
            for offset in OFFSETS:
                queue.append((i + offset[0], j + offset[1], distance + 1))
                
                
            
                
            
            
                