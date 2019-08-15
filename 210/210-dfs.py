from collections import defaultdict, deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        if not n:
            return []
        
        graph = defaultdict(list)
        visited = [0 for _ in range(n)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            
        stack = []
        for i in range(n):
            if visited[i] != 0:
                continue
                
            if not self.dfs(i, graph, visited, stack):
                return []
        
        
        return stack[::-1]
    
    
    def dfs(self, lesson, graph, visited, stack):
        if visited[lesson] == 1:
            return True
        
        if visited[lesson] == -1:
            return False
        
        visited[lesson] = -1
        for nei in graph[lesson]:
            if not self.dfs(nei, graph, visited, stack):
                return False
            
        stack.append(lesson)
        visited[lesson] = 1
        return True
                
        
        
        
        
        