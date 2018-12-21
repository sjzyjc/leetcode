from collections import defaultdict
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges and n > 1:
            return False
        
        graph = defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        seen = set()
        if self.hasCycle(graph, 0, seen, -1):
            return False
        
        return len(seen) == n
    
    def hasCycle(self, graph, node, seen, prev):
        if node in seen:
            return True
            
        seen.add(node)
        for nei in graph[node]:
            if nei == prev:
                continue
                
            if self.hasCycle(graph, nei, seen, node):
                return True
            
        return False
                
            
        