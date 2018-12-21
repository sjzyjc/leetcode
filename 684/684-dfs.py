from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        O(N^2)
        """
        if not edges:
            return []
        
        graph = defaultdict(set)
        for v1, v2 in edges:
            visited = set()
            if v1 in graph and v2 in graph and self.dfs(v1, v2, graph, visited):
                return v1, v2
            
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        return []
    
    def dfs(self, start, end, graph, visited):
        if start == end:
            return True
        
        if start in visited:
            return False
        
        visited.add(start)
        return any(self.dfs(i, end, graph, visited) for i in graph[start])
            