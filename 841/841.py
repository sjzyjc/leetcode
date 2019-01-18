from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return True
        
        graph = defaultdict(set)
        for index, room in enumerate(rooms):
            for key in room:
                graph[index].add(key)
                
        visited = set()
        stack = [0]

        while stack:
            node = stack.pop()
            visited.add(node)
            
            for nei in graph[node]:
                if nei in visited:
                    continue
                    
                stack.append(nei)
                
        return len(visited) == len(rooms)
                
            
        
        