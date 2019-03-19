class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        
        colored = {}
        for i in range(len(graph)):
            if i in colored:
                continue
                
            if self.cannotColor(graph, i, 0, colored):
                return False
            
        return True
    
    def cannotColor(self, graph, node, to_color, colored):
        if node in colored:
            return colored[node] != to_color
        
        colored[node] = to_color
        for nei in graph[node]:
            if self.cannotColor(graph, nei, 1 - to_color, colored):
                return True
            
        return False