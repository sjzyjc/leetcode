from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        
        count = defaultdict(int)
        graph = defaultdict(list)
        for depart, arrive in tickets:
            graph[depart].append(arrive)
            count[(depart, arrive)] += 1

            
        ans = []
        self.dfs("JFK", count, graph, ans)
        return ans[::-1]
    
    def dfs(self, node, count, graph, ans):
        for nei in sorted(graph[node]):
            edge = (node, nei)
            if count[edge] > 0:
                count[edge] -= 1
                self.dfs(nei, count, graph, ans)
                
        ans.append(node)
            
        
        