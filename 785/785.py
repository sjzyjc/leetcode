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
            
            if not self.canColor(graph, node, colored, 0):
                return False
            
        return True
    
    def canColor(self, graph, cur, colored, color):
        if cur in colored:
            if color == colored[cur]:
                return True
            else: 
                return False
            
        colored[cur] = color
        for nei in graph[cur]:
            if not self.canColor(graph, nei, colored, 1 - color):
                return False
        
        return True
            
        