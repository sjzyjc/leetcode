from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n < 0:
            return 0
        
        if not edges or not edges[0]:
            return n
        
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
            
        visited = set()
        ans = 0
        for i in range(n):
            if i in visited:
                continue
                
            self.traverse(i, graph, visited)
            ans += 1
            
        return ans
    
    def traverse(self, node, graph, visited):
        if node in visited:
            return
        
        visited.add(node)
        for nei in graph[node]:
            self.traverse(nei, graph, visited)
            
            