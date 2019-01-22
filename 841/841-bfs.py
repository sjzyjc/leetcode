from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return True
        
        queue = deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in rooms[node]:
                if nei in visited:
                    continue
                    
                queue.append(nei)
                       
        return len(visited) == len(rooms)
        
        