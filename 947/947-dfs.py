from collections import defaultdict
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:
            return 0
        
        graph = defaultdict(set)
        for i, stone in enumerate(stones):
            x1, y1 = stone
            
            for j in range(i + 1, len(stones)):
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    graph[i].add(j)
                    graph[j].add(i)
            
            seen = set()
            counter = 0
            for i in range(len(stones)):
                if i in seen:
                    continue
                    
                self.dfs(graph, i, seen)
                counter += 1
        
        return len(stones) - counter
    
    def dfs(self, graph, i, seen):
        if i in seen:
            return
        
        seen.add(i)
        for nei in graph[i]:
            self.dfs(graph, nei, seen)
            