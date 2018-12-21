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
            
            colored[node] = 0
            stack = [node]
            
            #dfs
            while stack:
                cur_node = stack.pop()
                cur_color = colored[cur_node]
                for nei in graph[cur_node]:
                    if nei not in colored:
                        colored[nei] = 1 - cur_color
                        stack.append(nei)
                    elif colored[nei] == cur_color:
                        return False
            
        return True

        