from collections import deque
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        
        #assume color 0 and 1
        colored = {}
        
        for node in range(len(graph)):
            if node in colored:
                continue
            
            queue = deque([node])
            colored[node] = 0
            
            while queue:
                length = len(queue)
                cur_color = colored[queue[0]]
                for _ in range(length):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in colored:
                            colored[nei] = 1 - cur_color
                            queue.append(nei)
                        elif colored[nei] == cur_color:
                            return False
                        
        return True
                    

        